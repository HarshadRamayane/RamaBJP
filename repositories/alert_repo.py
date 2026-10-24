"""
RamaBJP Alert Repository
Handles all database operations for alerts.
"""

from database.db import get_connection, now_iso


def get_all_alerts(limit=100):
    """Get all alerts, most recent first."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, e.name as equipment_name 
            FROM alerts a
            LEFT JOIN equipment e ON a.equipment_id = e.equipment_id
            ORDER BY a.created_at DESC
            LIMIT ?
        """, (limit,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_alert_by_id(alert_id):
    """Get a single alert by ID."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, e.name as equipment_name 
            FROM alerts a
            LEFT JOIN equipment e ON a.equipment_id = e.equipment_id
            WHERE a.alert_id = ?
        """, (alert_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_alerts_by_status(status, limit=100):
    """Get alerts filtered by status."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, e.name as equipment_name 
            FROM alerts a
            LEFT JOIN equipment e ON a.equipment_id = e.equipment_id
            WHERE a.status = ?
            ORDER BY a.created_at DESC
            LIMIT ?
        """, (status, limit))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_alerts_by_severity(severity, limit=100):
    """Get alerts filtered by severity."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, e.name as equipment_name 
            FROM alerts a
            LEFT JOIN equipment e ON a.equipment_id = e.equipment_id
            WHERE a.severity = ?
            ORDER BY a.created_at DESC
            LIMIT ?
        """, (severity, limit))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_alerts_for_equipment(equipment_id):
    """Get alerts for a specific equipment."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM alerts 
            WHERE equipment_id = ?
            ORDER BY created_at DESC
        """, (equipment_id,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def acknowledge_alert(alert_id, acknowledged_by="System"):
    """Acknowledge an alert."""
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE alerts 
            SET status = 'ACKNOWLEDGED', acknowledged_at = ?, acknowledged_by = ?
            WHERE alert_id = ? AND status = 'OPEN'
        """, (now, acknowledged_by, alert_id))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def resolve_alert(alert_id, resolution_notes="", resolved_by="System"):
    """Resolve an alert."""
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE alerts 
            SET status = 'RESOLVED', resolved_at = ?, resolved_by = ?, resolution_notes = ?
            WHERE alert_id = ? AND status IN ('OPEN', 'ACKNOWLEDGED')
        """, (now, resolved_by, resolution_notes, alert_id))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def delete_alert(alert_id):
    """Delete an alert (admin only)."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alerts WHERE alert_id = ?", (alert_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def get_alert_stats():
    """Get alert statistics."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM alerts")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT status, COUNT(*) FROM alerts GROUP BY status")
        by_status = {row[0]: row[1] for row in cursor.fetchall()}
        
        cursor.execute("SELECT severity, COUNT(*) FROM alerts GROUP BY severity")
        by_severity = {row[0]: row[1] for row in cursor.fetchall()}
        
        return {
            "total": total,
            "open": by_status.get("OPEN", 0),
            "acknowledged": by_status.get("ACKNOWLEDGED", 0),
            "resolved": by_status.get("RESOLVED", 0),
            "critical": by_severity.get("Critical", 0),
            "warning": by_severity.get("Warning", 0)
        }
    finally:
        conn.close()