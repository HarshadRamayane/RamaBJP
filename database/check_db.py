"""
RamaBJP Database Verification Script
Checks if all tables exist in the database.
"""

from database.db import get_connection


def check_tables():
    """Check all tables in the database."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = [row[0] for row in cursor.fetchall()]
        
        print("\n" + "=" * 50)
        print("RamaBJP Database Verification")
        print("=" * 50)
        
        if not tables:
            print("No tables found!")
            return
        
        print(f"\nFound {len(tables)} tables:\n")
        for i, table in enumerate(tables, 1):
            # Count rows in each table
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"  {i}. {table} ({count} rows)")
        
        print("\n" + "=" * 50)
        print("Database verification complete!")
        print("=" * 50 + "\n")
        
    finally:
        conn.close()


if __name__ == "__main__":
    check_tables()