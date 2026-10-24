"""
RamaBJP Database Connection Module
Handles SQLite database connections and initialization.
"""

import sqlite3
from pathlib import Path
from datetime import datetime, timezone


# Database file path
DB_DIR = Path(__file__).parent.parent / "data"
DB_PATH = DB_DIR / "ramabjp.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def get_connection():
    """Get a SQLite database connection."""
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_database():
    """Initialize database with schema."""
    conn = get_connection()
    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            schema = f.read()
        conn.executescript(schema)
        conn.commit()
        print(f"Database initialized at: {DB_PATH}")
    except Exception as e:
        print(f"Database initialization failed: {e}")
        raise
    finally:
        conn.close()


def execute_query(query, params=None):
    """Execute a query and return results."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        conn.commit()
        return cursor.fetchall()
    finally:
        conn.close()


def execute_insert(query, params=None):
    """Execute an insert and return last row id."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def fetch_one(query, params=None):
    """Fetch a single row."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        return cursor.fetchone()
    finally:
        conn.close()


def fetch_all(query, params=None):
    """Fetch all rows."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        return cursor.fetchall()
    finally:
        conn.close()


def now_iso():
    """Get current UTC timestamp in ISO format (timezone-aware)."""
    return datetime.now(timezone.utc).isoformat()


if __name__ == "__main__":
    init_database()