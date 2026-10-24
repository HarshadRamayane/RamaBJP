"""
RamaBJP Equipment Repository
Handles all database operations for equipment.
"""

from database.db import get_connection, now_iso


def get_all_equipment():
    """Get all equipment records."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipment ORDER BY equipment_id")
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_equipment_by_id(equipment_id):
    """Get a single equipment by ID."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipment WHERE equipment_id = ?", (equipment_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def add_equipment(equipment_id, name, category, manufacturer="", model="",
                  location="", status="Unknown", notes=""):
    """Add a new equipment record."""
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO equipment 
            (equipment_id, name, category, manufacturer, model, location, status, notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (equipment_id, name, category, manufacturer, model, location, status, notes, now, now))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding equipment: {e}")
        return False
    finally:
        conn.close()


def update_equipment(equipment_id, **kwargs):
    """Update an existing equipment record."""
    if not kwargs:
        return False
    
    allowed_fields = ["name", "category", "manufacturer", "model", 
                      "location", "status", "notes"]
    updates = {k: v for k, v in kwargs.items() if k in allowed_fields}
    
    if not updates:
        return False
    
    updates["updated_at"] = now_iso()
    
    set_clause = ", ".join([f"{k} = ?" for k in updates.keys()])
    values = list(updates.values()) + [equipment_id]
    
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE equipment SET {set_clause} WHERE equipment_id = ?", values)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating equipment: {e}")
        return False
    finally:
        conn.close()


def delete_equipment(equipment_id):
    """Delete an equipment record."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipment WHERE equipment_id = ?", (equipment_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting equipment: {e}")
        return False
    finally:
        conn.close()


def search_equipment(query):
    """Search equipment by ID or name."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM equipment 
            WHERE equipment_id LIKE ? OR name LIKE ?
            ORDER BY equipment_id
        """, (f"%{query}%", f"%{query}%"))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def filter_equipment(category=None, status=None):
    """Filter equipment by category and/or status."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM equipment WHERE 1=1"
        params = []
        
        if category:
            query += " AND category = ?"
            params.append(category)
        if status:
            query += " AND status = ?"
            params.append(status)
        
        query += " ORDER BY equipment_id"
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_equipment_stats():
    """Get equipment statistics."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM equipment")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT status, COUNT(*) FROM equipment GROUP BY status")
        by_status = {row[0]: row[1] for row in cursor.fetchall()}
        
        return {
            "total": total,
            "normal": by_status.get("Normal", 0),
            "warning": by_status.get("Warning", 0),
            "critical": by_status.get("Critical", 0),
            "unknown": by_status.get("Unknown", 0)
        }
    finally:
        conn.close()