"""
Tests for rule engine.
"""

import pytest
from database.db import get_connection
from rules.engine import (
    get_active_rules, get_rule_for_sensor_type,
    evaluate_reading, evaluate_equipment,
    evaluate_all_equipment, create_alert
)


def cleanup_test_equipment(eq_id="EQ-TEST"):
    """Remove test equipment if it exists."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alerts WHERE equipment_id = ?", (eq_id,))
        cursor.execute("DELETE FROM equipment WHERE equipment_id = ?", (eq_id,))
        conn.commit()
    finally:
        conn.close()


def test_get_active_rules():
    """Test getting active rules."""
    rules = get_active_rules()
    assert len(rules) == 8


def test_get_rule_for_sensor_type():
    """Test getting rule for sensor type."""
    rule = get_rule_for_sensor_type("vibration")
    assert rule is not None
    assert rule["sensor_type"] == "vibration"


def test_evaluate_reading_normal():
    """Test evaluating normal reading."""
    rule = get_rule_for_sensor_type("vibration")
    status, reason = evaluate_reading(0.2, rule)
    assert status == "Normal"


def test_evaluate_reading_warning():
    """Test evaluating warning reading."""
    rule = get_rule_for_sensor_type("vibration")
    status, reason = evaluate_reading(0.5, rule)
    assert status == "Warning"


def test_evaluate_reading_critical():
    """Test evaluating critical reading."""
    rule = get_rule_for_sensor_type("vibration")
    status, reason = evaluate_reading(0.7, rule)
    assert status == "Critical"


def test_evaluate_reading_less_than_rule():
    """Test less-than rule (oil quality)."""
    rule = get_rule_for_sensor_type("oil_quality")
    status, reason = evaluate_reading(30, rule)
    assert status == "Critical"


def test_evaluate_reading_no_rule():
    """Test with no rule."""
    status, reason = evaluate_reading(0.5, None)
    assert status == "Unknown"


def test_evaluate_reading_none_value():
    """Test with None value."""
    rule = get_rule_for_sensor_type("vibration")
    status, reason = evaluate_reading(None, rule)
    assert status == "Unknown"


def test_evaluate_equipment():
    """Test evaluating equipment."""
    results = evaluate_equipment("EQ-001")
    assert len(results) > 0


def test_evaluate_all_equipment():
    """Test evaluating all equipment."""
    # Cleanup test equipment first
    cleanup_test_equipment("EQ-TEST")
    
    results = evaluate_all_equipment()
    assert len(results) >= 15


def test_create_alert():
    """Test creating an alert."""
    # Create EQ-TEST equipment for foreign key
    from repositories.equipment_repo import add_equipment, get_equipment_by_id
    if not get_equipment_by_id("EQ-TEST"):
        add_equipment("EQ-TEST", "Test Equipment", "Test")
    
    # Clean up existing alerts
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM alerts 
            WHERE equipment_id = ? AND sensor_id = ? AND severity = ?
        """, ("EQ-TEST", "SENSOR-VIB", "Critical"))
        conn.commit()
    finally:
        conn.close()
    
    # Now create the alert
    alert_id = create_alert(
        "EQ-TEST", "SENSOR-VIB", "Critical",
        "Test alert", 0.9, 0.6, "RULE-VIB-001"
    )
    assert alert_id is not None