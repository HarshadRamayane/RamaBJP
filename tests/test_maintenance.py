"""
Tests for maintenance work order repository.
"""

import pytest
from database.db import get_connection
from repositories.maintenance_repo import (
    create_work_order, get_all_work_orders, get_work_order_by_id,
    get_work_orders_by_status, get_work_orders_for_equipment,
    update_work_order_status, assign_work_order, delete_work_order,
    get_work_order_stats
)


def cleanup_test_work_orders():
    """Remove test work orders."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM work_orders WHERE equipment_id = 'EQ-001'")
        conn.commit()
    finally:
        conn.close()


def test_create_work_order():
    """Test creating a work order."""
    cleanup_test_work_orders()
    wo_id = create_work_order(
        "EQ-001", "Test issue", "High", "tech1", "2026-10-20", "Test notes"
    )
    assert wo_id is not None
    assert wo_id.startswith("WO-")


def test_get_all_work_orders():
    """Test getting all work orders."""
    work_orders = get_all_work_orders()
    assert isinstance(work_orders, list)


def test_get_work_order_by_id():
    """Test getting a work order by ID."""
    cleanup_test_work_orders()
    wo_id = create_work_order("EQ-001", "Test issue", "High")
    
    wo = get_work_order_by_id(wo_id)
    assert wo is not None
    assert wo["equipment_id"] == "EQ-001"
    assert wo["issue"] == "Test issue"
    assert wo["priority"] == "High"


def test_get_work_orders_by_status():
    """Test filtering work orders by status."""
    work_orders = get_work_orders_by_status("Open")
    assert isinstance(work_orders, list)


def test_get_work_orders_for_equipment():
    """Test getting work orders for equipment."""
    cleanup_test_work_orders()
    create_work_order("EQ-001", "Test issue", "High")
    work_orders = get_work_orders_for_equipment("EQ-001")
    assert len(work_orders) > 0


def test_update_work_order_status():
    """Test updating work order status."""
    cleanup_test_work_orders()
    wo_id = create_work_order("EQ-001", "Test issue", "High")
    
    result = update_work_order_status(wo_id, "In Progress", notes="Working on it")
    assert result is True
    
    wo = get_work_order_by_id(wo_id)
    assert wo["status"] == "In Progress"


def test_complete_work_order():
    """Test completing a work order."""
    cleanup_test_work_orders()
    wo_id = create_work_order("EQ-001", "Test issue", "High")
    
    result = update_work_order_status(
        wo_id, "Completed", 
        work_performed="Replaced bearing", 
        notes="All good"
    )
    assert result is True
    
    wo = get_work_order_by_id(wo_id)
    assert wo["status"] == "Completed"
    assert wo["work_performed"] == "Replaced bearing"


def test_assign_work_order():
    """Test assigning work order to technician."""
    cleanup_test_work_orders()
    wo_id = create_work_order("EQ-001", "Test issue", "High")
    
    result = assign_work_order(wo_id, "tech2")
    assert result is True
    
    wo = get_work_order_by_id(wo_id)
    assert wo["assigned_to"] == "tech2"


def test_delete_work_order():
    """Test deleting a work order."""
    cleanup_test_work_orders()
    wo_id = create_work_order("EQ-001", "Test issue", "High")
    
    result = delete_work_order(wo_id)
    assert result is True
    
    wo = get_work_order_by_id(wo_id)
    assert wo is None


def test_get_work_order_stats():
    """Test work order statistics."""
    stats = get_work_order_stats()
    assert "total" in stats
    assert "open" in stats
    assert "completed" in stats
    assert "high_priority" in stats