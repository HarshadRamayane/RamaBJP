"""
RamaBJP Maintenance Work Order Repository
Handles all database operations for maintenance work orders.
"""

from database.db import get_connection, now_iso


def generate_work_order_id():
    """Generate a unique work order ID."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM work_orders")
        count = cursor.fetchone()[0]
        return f"WO-{count + 1:04d}"
    finally:
        conn.close()


def create_work_order(equipment_id, issue, priority="Medium",
                      assigned_to="", planned_date="", notes=""):
    """Create a new work order."""
    wo_id = generate_work_order_id()
    now = now_iso()
    
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO work_orders 
            (work_order_id, equipment_id, issue, priority, status, 
             assigned_to, planned_date, notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, 'Open', ?, ?, ?, ?, ?)
        """, (wo_id, equipment_id, issue, priority, assigned_to, 
              planned_date, notes, now, now))
        conn.commit()
        return wo_id
    except Exception as e:
        print(f"Error creating work order: {e}")
        return None
    finally:
        conn.close()


def get_all_work_orders(limit=100):
    """Get all work orders."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT wo.*, e.name as equipment_name
            FROM work_orders wo
            LEFT JOIN equipment e ON wo.equipment_id = e.equipment_id
            ORDER BY wo.created_at DESC
            LIMIT ?
        """, (limit,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_work_order_by_id(work_order_id):
    """Get a single work order by ID."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT wo.*, e.name as equipment_name
            FROM work_orders wo
            LEFT JOIN equipment e ON wo.equipment_id = e.equipment_id
            WHERE wo.work_order_id = ?
        """, (work_order_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def get_work_orders_by_status(status, limit=100):
    """Get work orders filtered by status."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT wo.*, e.name as equipment_name
            FROM work_orders wo
            LEFT JOIN equipment e ON wo.equipment_id = e.equipment_id
            WHERE wo.status = ?
            ORDER BY wo.created_at DESC
            LIMIT ?
        """, (status, limit))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def get_work_orders_for_equipment(equipment_id):
    """Get work orders for a specific equipment."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM work_orders 
            WHERE equipment_id = ?
            ORDER BY created_at DESC
        """, (equipment_id,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


def update_work_order_status(work_order_id, status, work_performed="", notes=""):
    """Update work order status."""
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        if status == "Completed":
            cursor.execute("""
                UPDATE work_orders 
                SET status = ?, completed_date = ?, work_performed = ?, 
                    notes = ?, updated_at = ?
                WHERE work_order_id = ?
            """, (status, now, work_performed, notes, now, work_order_id))
        else:
            cursor.execute("""
                UPDATE work_orders 
                SET status = ?, notes = ?, updated_at = ?
                WHERE work_order_id = ?
            """, (status, notes, now, work_order_id))
        
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def assign_work_order(work_order_id, assigned_to):
    """Assign a work order to a technician."""
    now = now_iso()
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE work_orders 
            SET assigned_to = ?, updated_at = ?
            WHERE work_order_id = ?
        """, (assigned_to, now, work_order_id))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def delete_work_order(work_order_id):
    """Delete a work order."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM work_orders WHERE work_order_id = ?", (work_order_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def get_work_order_stats():
    """Get work order statistics."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM work_orders")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT status, COUNT(*) FROM work_orders GROUP BY status")
        by_status = {row[0]: row[1] for row in cursor.fetchall()}
        
        cursor.execute("SELECT priority, COUNT(*) FROM work_orders GROUP BY priority")
        by_priority = {row[0]: row[1] for row in cursor.fetchall()}
        
        return {
            "total": total,
            "open": by_status.get("Open", 0),
            "in_progress": by_status.get("In Progress", 0),
            "completed": by_status.get("Completed", 0),
            "high_priority": by_priority.get("High", 0),
            "critical_priority": by_priority.get("Critical", 0)
        }
    finally:
        conn.close()


def get_overdue_work_orders():
    """Get overdue work orders (planned_date < today, status not Completed)."""
    today = datetime.now().strftime("%Y-%m-%d")
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT wo.*, e.name as equipment_name
            FROM work_orders wo
            LEFT JOIN equipment e ON wo.equipment_id = e.equipment_id
            WHERE wo.planned_date < ? 
            AND wo.status != 'Completed'
            AND wo.planned_date != ''
            ORDER BY wo.planned_date
        """, (today,))
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


from datetime import datetime