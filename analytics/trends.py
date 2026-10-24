"""
RamaBJP Analytics - Trends Module
Provides trend analysis for sensor readings.
"""

from database.db import get_connection
from datetime import datetime, timedelta


def get_sensor_trend(equipment_id, sensor_id, days=7):
    """Get trend data for a specific sensor."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        
        cursor.execute("""
            SELECT timestamp, value, unit
            FROM sensor_readings
            WHERE equipment_id = ? AND sensor_id = ?
            AND timestamp >= ?
            ORDER BY timestamp ASC
        """, (equipment_id, sensor_id, cutoff))
        
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_equipment_trends(equipment_id, days=7):
    """Get all sensor trends for an equipment."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        
        cursor.execute("""
            SELECT sensor_id, timestamp, value, unit
            FROM sensor_readings
            WHERE equipment_id = ?
            AND timestamp >= ?
            ORDER BY sensor_id, timestamp ASC
        """, (equipment_id, cutoff))
        
        rows = [dict(row) for row in cursor.fetchall()]
        
        # Group by sensor
        trends = {}
        for row in rows:
            sid = row["sensor_id"]
            if sid not in trends:
                trends[sid] = []
            trends[sid].append({
                "timestamp": row["timestamp"],
                "value": row["value"],
                "unit": row["unit"]
            })
        
        return trends
    finally:
        conn.close()


def get_equipment_status_distribution():
    """Get equipment status distribution."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT status, COUNT(*) as count
            FROM equipment
            GROUP BY status
        """)
        return {row[0]: row[1] for row in cursor.fetchall()}
    finally:
        conn.close()


def get_alert_frequency(days=30):
    """Get alert frequency over time."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        
        cursor.execute("""
            SELECT DATE(created_at) as date, severity, COUNT(*) as count
            FROM alerts
            WHERE created_at >= ?
            GROUP BY DATE(created_at), severity
            ORDER BY date
        """, (cutoff,))
        
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_maintenance_status_distribution():
    """Get work order status distribution."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT status, COUNT(*) as count
            FROM work_orders
            GROUP BY status
        """)
        return {row[0]: row[1] for row in cursor.fetchall()}
    finally:
        conn.close()


def get_data_completeness():
    """Get data completeness stats."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM equipment")
        total_equipment = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM equipment_sensors WHERE is_active = 1")
        total_mappings = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM sensor_readings")
        total_readings = cursor.fetchone()[0]
        
        return {
            "total_equipment": total_equipment,
            "total_mappings": total_mappings,
            "total_readings": total_readings,
            "avg_readings_per_equipment": round(total_readings / total_equipment, 2) if total_equipment > 0 else 0
        }
    finally:
        conn.close()


def get_summary_stats():
    """Get overall summary statistics."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM equipment")
        equipment_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM sensor_readings")
        readings_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM alerts WHERE status = 'OPEN'")
        open_alerts = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM work_orders WHERE status != 'Completed'")
        open_work_orders = cursor.fetchone()[0]
        
        return {
            "total_equipment": equipment_count,
            "total_readings": readings_count,
            "open_alerts": open_alerts,
            "open_work_orders": open_work_orders
        }
    finally:
        conn.close()