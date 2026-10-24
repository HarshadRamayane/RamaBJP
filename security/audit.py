"""
RamaBJP Audit Logging Module
Records important user actions.
"""

from database.db import get_connection, now_iso


def log_event(actor, action, entity_type=None, entity_id=None, details=None):
    """Log an audit event."""
    timestamp = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO audit_events 
            (actor, action, entity_type, entity_id, details, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (actor, action, entity_type, entity_id, details, timestamp))
        conn.commit()
        return True
    except Exception as e:
        print(f"Audit log error: {e}")
        return False
    finally:
        conn.close()


def get_recent_events(limit=50):
    """Get recent audit events."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM audit_events 
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (limit,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_events_by_actor(actor, limit=50):
    """Get audit events by actor."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM audit_events 
            WHERE actor = ?
            ORDER BY timestamp DESC 
            LIMIT ?
        """, (actor, limit))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def clear_audit_log():
    """Clear all audit events (admin only)."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM audit_events")
        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()