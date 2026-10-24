"""
Tests for equipment repository.
"""

import pytest
from database.db import get_connection
from repositories.equipment_repo import (
    get_all_equipment, get_equipment_by_id,
    add_equipment, update_equipment, delete_equipment,
    search_equipment, get_equipment_stats
)


def cleanup_test_equipment(eq_id="EQ-TEST"):
    """Remove test equipment if it exists."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipment WHERE equipment_id = ?", (eq_id,))
        conn.commit()
    finally:
        conn.close()


def test_get_all_equipment():
    """Test getting all equipment."""
    equipment = get_all_equipment()
    assert len(equipment) >= 15


def test_get_equipment_by_id():
    """Test getting equipment by ID."""
    eq = get_equipment_by_id("EQ-001")
    assert eq is not None
    assert eq["equipment_id"] == "EQ-001"


def test_add_equipment():
    """Test adding new equipment."""
    cleanup_test_equipment("EQ-TEST")
    result = add_equipment("EQ-TEST", "Test Equipment", "Test Category")
    assert result is True
    
    eq = get_equipment_by_id("EQ-TEST")
    assert eq is not None
    assert eq["name"] == "Test Equipment"
    
    cleanup_test_equipment("EQ-TEST")


def test_update_equipment():
    """Test updating equipment."""
    cleanup_test_equipment("EQ-UPD")
    add_equipment("EQ-UPD", "Old Name", "Category")
    result = update_equipment("EQ-UPD", name="New Name", status="Warning")
    assert result is True
    
    eq = get_equipment_by_id("EQ-UPD")
    assert eq["name"] == "New Name"
    assert eq["status"] == "Warning"
    
    cleanup_test_equipment("EQ-UPD")


def test_search_equipment():
    """Test searching equipment."""
    results = search_equipment("Engine")
    assert len(results) > 0


def test_get_equipment_stats():
    """Test equipment statistics."""
    stats = get_equipment_stats()
    assert stats["total"] >= 15
    assert "normal" in stats
    assert "warning" in stats
    assert "critical" in stats


def test_delete_equipment():
    """Test deleting equipment."""
    cleanup_test_equipment("EQ-DEL")
    add_equipment("EQ-DEL", "Delete Me", "Test")
    result = delete_equipment("EQ-DEL")
    assert result is True
    
    eq = get_equipment_by_id("EQ-DEL")
    assert eq is None