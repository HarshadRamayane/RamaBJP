"""
Tests for alert repository.
"""

import pytest
from database.db import get_connection
from repositories.alert_repo import (
    get_all_alerts, get_alert_by_id,
    get_alerts_by_status, get_alerts_by_severity,
    get_alerts_for_equipment, acknowledge_alert,
    resolve_alert, delete_alert, get_alert_stats
)
from repositories.equipment_repo import add_equipment, delete_equipment, get_equipment_by_id
from rules.engine import create_alert


def setup_test_equipment():
    """Create EQ-TEST equipment if it doesn't exist."""
    existing = get_equipment_by_id("EQ-TEST")
    if not existing:
        add_equipment("EQ-TEST", "Test Equipment", "Test Category",
                      manufacturer="Test", model="T-001", location="Test Lab")


def setup_test_alert():
    """Create a test alert for testing."""
    # Ensure equipment exists
    setup_test_equipment()
    
    # Clean up existing alerts
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alerts WHERE equipment_id = 'EQ-TEST'")
        conn.commit()
    finally:
        conn.close()
    
    # Create new alert
    return create_alert(
        "EQ-TEST", "SENSOR-VIB", "Critical",
        "Test alert for testing", 0.9, 0.6, "RULE-VIB-001"
    )


def test_get_all_alerts():
    """Test getting all alerts."""
    alerts = get_all_alerts()
    assert isinstance(alerts, list)


def test_create_and_get_alert():
    """Test creating and getting an alert."""
    alert_id = setup_test_alert()
    assert alert_id is not None
    
    alert = get_alert_by_id(alert_id)
    assert alert is not None
    assert alert["equipment_id"] == "EQ-TEST"
    assert alert["severity"] == "Critical"
    assert alert["status"] == "OPEN"


def test_get_alerts_by_status():
    """Test filtering alerts by status."""
    alerts = get_alerts_by_status("OPEN")
    assert isinstance(alerts, list)


def test_get_alerts_by_severity():
    """Test filtering alerts by severity."""
    alerts = get_alerts_by_severity("Critical")
    assert isinstance(alerts, list)


def test_get_alerts_for_equipment():
    """Test getting alerts for specific equipment."""
    setup_test_alert()
    alerts = get_alerts_for_equipment("EQ-TEST")
    assert len(alerts) > 0


def test_acknowledge_alert():
    """Test acknowledging an alert."""
    alert_id = setup_test_alert()
    result = acknowledge_alert(alert_id, "test_user")
    assert result is True
    
    alert = get_alert_by_id(alert_id)
    assert alert["status"] == "ACKNOWLEDGED"
    assert alert["acknowledged_by"] == "test_user"


def test_resolve_alert():
    """Test resolving an alert."""
    alert_id = setup_test_alert()
    acknowledge_alert(alert_id, "test_user")
    result = resolve_alert(alert_id, "Fixed the issue", "test_user")
    assert result is True
    
    alert = get_alert_by_id(alert_id)
    assert alert["status"] == "RESOLVED"
    assert alert["resolution_notes"] == "Fixed the issue"


def test_delete_alert():
    """Test deleting an alert."""
    alert_id = setup_test_alert()
    result = delete_alert(alert_id)
    assert result is True
    
    alert = get_alert_by_id(alert_id)
    assert alert is None


def test_get_alert_stats():
    """Test alert statistics."""
    stats = get_alert_stats()
    assert "total" in stats
    assert "open" in stats
    assert "acknowledged" in stats
    assert "resolved" in stats
    assert "critical" in stats
    assert "warning" in stats