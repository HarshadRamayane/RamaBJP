"""
RamaBJP Cleanup Script
Removes test data from the database.
"""

from database.db import get_connection


def cleanup_test_data():
    """Remove all test equipment and related data."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        # Delete alerts for EQ-TEST
        cursor.execute("DELETE FROM alerts WHERE equipment_id = 'EQ-TEST'")
        alerts_deleted = cursor.rowcount
        
        # Delete work orders for EQ-TEST
        cursor.execute("DELETE FROM work_orders WHERE equipment_id = 'EQ-TEST'")
        wo_deleted = cursor.rowcount
        
        # Delete equipment_sensors for EQ-TEST
        cursor.execute("DELETE FROM equipment_sensors WHERE equipment_id = 'EQ-TEST'")
        sensors_deleted = cursor.rowcount
        
        # Delete EQ-TEST equipment
        cursor.execute("DELETE FROM equipment WHERE equipment_id = 'EQ-TEST'")
        eq_deleted = cursor.rowcount
        
        conn.commit()
        
        print("=" * 50)
        print("Cleanup Complete")
        print("=" * 50)
        print(f"Alerts deleted: {alerts_deleted}")
        print(f"Work orders deleted: {wo_deleted}")
        print(f"Sensor mappings deleted: {sensors_deleted}")
        print(f"Equipment deleted: {eq_deleted}")
        print("=" * 50)
        
        # Verify
        cursor.execute("SELECT COUNT(*) FROM equipment")
        total = cursor.fetchone()[0]
        print(f"Total equipment remaining: {total}")
        print("=" * 50)
        
    finally:
        conn.close()


if __name__ == "__main__":
    cleanup_test_data()