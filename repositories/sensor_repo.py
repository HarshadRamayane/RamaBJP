"""
RamaBJP Sensor Repository
Handles all database operations for sensors and readings.
"""

from database.db import get_connection, now_iso


# ============================================================
# SENSOR DEFINITIONS
# ============================================================

def get_all_sensor_definitions():
    """Get all sensor definitions."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sensor_definitions ORDER BY sensor_id")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_sensor_by_id(sensor_id):
    """Get a single sensor definition by ID."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sensor_definitions WHERE sensor_id = ?", (sensor_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_sensor_by_type(sensor_type):
    """Get sensor definition by type."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sensor_definitions WHERE sensor_type = ?", (sensor_type,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


# ============================================================
# EQUIPMENT-SENSOR MAPPINGS
# ============================================================

def get_sensors_for_equipment(equipment_id):
    """Get all sensors mapped to an equipment."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT sd.* FROM sensor_definitions sd
            INNER JOIN equipment_sensors es ON sd.sensor_id = es.sensor_id
            WHERE es.equipment_id = ? AND es.is_active = 1
            ORDER BY sd.sensor_id
        """, (equipment_id,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_equipment_for_sensor(sensor_id):
    """Get all equipment mapped to a sensor."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT e.* FROM equipment e
            INNER JOIN equipment_sensors es ON e.equipment_id = es.equipment_id
            WHERE es.sensor_id = ? AND es.is_active = 1
            ORDER BY e.equipment_id
        """, (sensor_id,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


# ============================================================
# SENSOR READINGS
# ============================================================

def add_reading(equipment_id, sensor_id, value, unit, source="DEMO", quality="Good"):
    """Add a new sensor reading."""
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sensor_readings 
            (equipment_id, sensor_id, timestamp, value, unit, source, quality, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (equipment_id, sensor_id, now, value, unit, source, quality, now))
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def get_latest_reading(equipment_id, sensor_id):
    """Get the latest reading for an equipment-sensor pair."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM sensor_readings 
            WHERE equipment_id = ? AND sensor_id = ?
            ORDER BY timestamp DESC LIMIT 1
        """, (equipment_id, sensor_id))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_readings_for_equipment(equipment_id, limit=100):
    """Get readings for an equipment."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM sensor_readings 
            WHERE equipment_id = ?
            ORDER BY timestamp DESC LIMIT ?
        """, (equipment_id, limit))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_readings_by_sensor(sensor_id, limit=100):
    """Get readings for a sensor type."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM sensor_readings 
            WHERE sensor_id = ?
            ORDER BY timestamp DESC LIMIT ?
        """, (sensor_id, limit))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_all_readings(limit=500):
    """Get all recent readings."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM sensor_readings 
            ORDER BY timestamp DESC LIMIT ?
        """, (limit,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


# ============================================================
# STATISTICS
# ============================================================

def get_sensor_stats():
    """Get sensor statistics."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM sensor_definitions")
        total_sensors = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM equipment_sensors WHERE is_active = 1")
        total_mappings = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM sensor_readings")
        total_readings = cursor.fetchone()[0]
        
        return {
            "total_sensors": total_sensors,
            "total_mappings": total_mappings,
            "total_readings": total_readings
        }
    finally:
        conn.close()


def get_readings_count_by_sensor():
    """Get reading count grouped by sensor."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT sensor_id, COUNT(*) as count 
            FROM sensor_readings 
            GROUP BY sensor_id
            ORDER BY sensor_id
        """)
        return {row[0]: row[1] for row in cursor.fetchall()}
    finally:
        conn.close()