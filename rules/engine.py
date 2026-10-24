"""
RamaBJP Rule Engine
Evaluates sensor readings against configured rules.
"""

from database.db import get_connection, now_iso
from repositories.sensor_repo import get_latest_reading, get_sensor_by_type


def get_active_rules():
    """Get all enabled rules."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rule_definitions WHERE enabled = 1")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_rule_for_sensor_type(sensor_type):
    """Get rule for a sensor type."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM rule_definitions 
            WHERE sensor_type = ? AND enabled = 1
            LIMIT 1
        """, (sensor_type,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def evaluate_reading(value, rule):
    """
    Evaluate a reading against a rule.
    Returns: status (Normal/Warning/Critical/Unknown), reason
    """
    if rule is None:
        return "Unknown", "No rule configured"
    
    if value is None:
        return "Unknown", "No reading available"
    
    warning = rule["warning_threshold"]
    critical = rule["critical_threshold"]
    direction = rule["comparison_direction"]
    
    if warning is None or critical is None:
        return "Unknown", "Thresholds not configured"
    
    if direction == "greater_than":
        if value > critical:
            return "Critical", f"Value {value} > critical threshold {critical}"
        elif value > warning:
            return "Warning", f"Value {value} > warning threshold {warning}"
        else:
            return "Normal", f"Value {value} within normal range"
    
    elif direction == "less_than":
        if value < critical:
            return "Critical", f"Value {value} < critical threshold {critical}"
        elif value < warning:
            return "Warning", f"Value {value} < warning threshold {warning}"
        else:
            return "Normal", f"Value {value} within normal range"
    
    return "Unknown", "Invalid comparison direction"


def create_alert(equipment_id, sensor_id, severity, message, reading_value, threshold_value, rule_id):
    """Create an alert in the database."""
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        # Check for duplicate alert (same equipment, sensor, severity, OPEN status)
        cursor.execute("""
            SELECT alert_id FROM alerts 
            WHERE equipment_id = ? AND sensor_id = ? 
            AND severity = ? AND status = 'OPEN'
        """, (equipment_id, sensor_id, severity))
        
        existing = cursor.fetchone()
        if existing:
            return None  # Skip duplicate
        
        cursor.execute("""
            INSERT INTO alerts 
            (equipment_id, sensor_id, severity, status, message, 
             reading_value, threshold_value, rule_id, created_at)
            VALUES (?, ?, ?, 'OPEN', ?, ?, ?, ?, ?)
        """, (equipment_id, sensor_id, severity, message,
              reading_value, threshold_value, rule_id, now))
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def evaluate_equipment(equipment_id):
    """Evaluate all sensors for an equipment."""
    from repositories.sensor_repo import get_sensors_for_equipment
    
    results = []
    sensors = get_sensors_for_equipment(equipment_id)
    
    for sensor in sensors:
        sensor_id = sensor["sensor_id"]
        sensor_type = sensor["sensor_type"]
        unit = sensor["unit"]
        
        # Get latest reading
        reading = get_latest_reading(equipment_id, sensor_id)
        value = reading["value"] if reading else None
        
        # Get rule
        rule = get_rule_for_sensor_type(sensor_type)
        
        # Evaluate
        status, reason = evaluate_reading(value, rule)
        
        result = {
            "sensor_id": sensor_id,
            "sensor_type": sensor_type,
            "unit": unit,
            "value": value,
            "status": status,
            "reason": reason,
            "rule_id": rule["rule_id"] if rule else None,
            "warning_threshold": rule["warning_threshold"] if rule else None,
            "critical_threshold": rule["critical_threshold"] if rule else None
        }
        results.append(result)
        
        # Create alert if Warning or Critical
        if status in ["Warning", "Critical"] and reading:
            threshold = rule["critical_threshold"] if status == "Critical" else rule["warning_threshold"]
            message = f"{sensor['name']}: {reason}"
            create_alert(equipment_id, sensor_id, status, message, value, threshold, rule["rule_id"])
    
    return results


def evaluate_all_equipment():
    """Evaluate all equipment."""
    from repositories.equipment_repo import get_all_equipment
    
    equipment_list = get_all_equipment()
    all_results = {}
    
    for eq in equipment_list:
        eq_id = eq["equipment_id"]
        all_results[eq_id] = evaluate_equipment(eq_id)
    
    return all_results