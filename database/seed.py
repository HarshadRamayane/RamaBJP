"""
RamaBJP Database Seed Script
Populates the database with synthetic demo data.
"""

from database.db import get_connection, now_iso


def seed_sensor_definitions():
    """Insert 8 sensor definitions."""
    sensors = [
        ("SENSOR-VIB", "vibration", "Vibration Sensor", "RMS", "Measures machine vibration"),
        ("SENSOR-TEMP", "temperature", "Temperature Sensor", "°C", "Measures component temperature"),
        ("SENSOR-OIL", "oil_quality", "Oil Quality Sensor", "%", "Measures oil condition"),
        ("SENSOR-ACOU", "acoustic", "Acoustic Sensor", "dB", "Measures sound pressure"),
        ("SENSOR-PRES", "pressure", "Pressure Sensor", "bar", "Measures fluid pressure"),
        ("SENSOR-CURR", "current", "Current Sensor", "A", "Measures electrical current"),
        ("SENSOR-RPM", "rpm", "RPM Sensor", "RPM", "Measures rotational speed"),
        ("SENSOR-ULTRA", "ultrasonic", "Ultrasonic Sensor", "mm", "Measures distance/thickness"),
    ]
    
    conn = get_connection()
    try:
        cursor = conn.cursor()
        for sensor in sensors:
            cursor.execute("""
                INSERT OR IGNORE INTO sensor_definitions 
                (sensor_id, sensor_type, name, unit, description)
                VALUES (?, ?, ?, ?, ?)
            """, sensor)
        conn.commit()
        print(f"Inserted {len(sensors)} sensor definitions")
    finally:
        conn.close()


def seed_equipment():
    """Insert 15 synthetic equipment records."""
    equipment_data = [
        ("EQ-001", "Engine Assembly", "Engine", "Demo Mfg", "M-100", "Pune MRO", "Normal"),
        ("EQ-002", "Gearbox Unit", "Transmission", "Demo Mfg", "G-200", "Nashik Unit", "Warning"),
        ("EQ-003", "Hydraulic Pump", "Hydraulic", "Demo Mfg", "H-300", "Nagpur Unit", "Critical"),
        ("EQ-004", "Radar Module", "Electronics", "Demo Mfg", "R-400", "Mumbai Unit", "Normal"),
        ("EQ-005", "Artillery Breech", "Weapon System", "Demo Mfg", "A-500", "Pune MRO", "Warning"),
        ("EQ-006", "Tank Transmission", "Transmission", "Demo Mfg", "T-600", "Nashik Unit", "Normal"),
        ("EQ-007", "Cooling System", "Cooling", "Demo Mfg", "C-700", "Nagpur Unit", "Normal"),
        ("EQ-008", "Electrical Generator", "Electrical", "Demo Mfg", "E-800", "Mumbai Unit", "Critical"),
        ("EQ-009", "Fuel Injector", "Engine", "Demo Mfg", "F-900", "Pune MRO", "Normal"),
        ("EQ-010", "Suspension Unit", "Suspension", "Demo Mfg", "S-1000", "Nashik Unit", "Warning"),
        ("EQ-011", "Turret Motor", "Weapon System", "Demo Mfg", "TM-1100", "Nagpur Unit", "Critical"),
        ("EQ-012", "Communication Array", "Electronics", "Demo Mfg", "CA-1200", "Mumbai Unit", "Normal"),
        ("EQ-013", "Navigation System", "Electronics", "Demo Mfg", "NS-1300", "Pune MRO", "Normal"),
        ("EQ-014", "Air Compressor", "Hydraulic", "Demo Mfg", "AC-1400", "Nashik Unit", "Normal"),
        ("EQ-015", "Hydraulic Valve", "Hydraulic", "Demo Mfg", "HV-1500", "Nagpur Unit", "Warning"),
    ]
    
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        for eq in equipment_data:
            cursor.execute("""
                INSERT OR IGNORE INTO equipment 
                (equipment_id, name, category, manufacturer, model, location, status, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (*eq, now, now))
        conn.commit()
        print(f"Inserted {len(equipment_data)} equipment records")
    finally:
        conn.close()


def seed_equipment_sensors():
    """Map ALL 8 sensors to each equipment."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        # Clear existing mappings
        cursor.execute("DELETE FROM equipment_sensors")
        
        cursor.execute("SELECT equipment_id FROM equipment ORDER BY equipment_id")
        equipment_ids = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT sensor_id FROM sensor_definitions ORDER BY sensor_id")
        sensor_ids = [row[0] for row in cursor.fetchall()]
        
        now = now_iso()
        count = 0
        for eq_id in equipment_ids:
            for sensor_id in sensor_ids:
                cursor.execute("""
                    INSERT OR IGNORE INTO equipment_sensors 
                    (equipment_id, sensor_id, installed_at, is_active)
                    VALUES (?, ?, ?, 1)
                """, (eq_id, sensor_id, now))
                count += 1
        
        conn.commit()
        print(f"Inserted {count} equipment-sensor mappings")
    finally:
        conn.close()


def seed_rules():
    """Insert rule definitions."""
    rules = [
        ("RULE-VIB-001", "vibration", "RMS", 0.4, 0.6, "greater_than", 
         "Vibration warning and critical thresholds", 1, "1.0"),
        ("RULE-TEMP-001", "temperature", "°C", 65.0, 80.0, "greater_than", 
         "Temperature warning and critical thresholds", 1, "1.0"),
        ("RULE-OIL-001", "oil_quality", "%", 60.0, 40.0, "less_than", 
         "Oil quality warning and critical thresholds", 1, "1.0"),
        ("RULE-PRES-001", "pressure", "bar", 3.0, 2.0, "less_than", 
         "Pressure warning and critical thresholds", 1, "1.0"),
        ("RULE-CURR-001", "current", "A", 50.0, 60.0, "greater_than", 
         "Current warning and critical thresholds", 1, "1.0"),
        ("RULE-RPM-001", "rpm", "RPM", 1500, 1200, "less_than", 
         "RPM warning and critical thresholds", 1, "1.0"),
        ("RULE-ACOU-001", "acoustic", "dB", 75.0, 85.0, "greater_than", 
         "Acoustic warning and critical thresholds", 1, "1.0"),
        ("RULE-ULTRA-001", "ultrasonic", "mm", 5.0, 3.0, "less_than", 
         "Ultrasonic warning and critical thresholds", 1, "1.0"),
    ]
    
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        for rule in rules:
            cursor.execute("""
                INSERT OR IGNORE INTO rule_definitions 
                (rule_id, sensor_type, unit, warning_threshold, critical_threshold, 
                 comparison_direction, description, enabled, version, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (*rule, now, now))
        conn.commit()
        print(f"Inserted {len(rules)} rule definitions")
    finally:
        conn.close()


def seed_all():
    """Run all seed functions."""
    print("\n" + "=" * 50)
    print("RamaBJP Database Seeding")
    print("=" * 50 + "\n")
    
    seed_sensor_definitions()
    seed_equipment()
    seed_equipment_sensors()
    seed_rules()
    
    print("\n" + "=" * 50)
    print("Seeding complete!")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    seed_all()