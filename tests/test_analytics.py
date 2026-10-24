"""
Tests for analytics module.
"""

import pytest
from analytics.trends import (
    get_sensor_trend, get_equipment_trends,
    get_equipment_status_distribution, get_alert_frequency,
    get_maintenance_status_distribution, get_data_completeness,
    get_summary_stats
)


def test_get_sensor_trend():
    """Test getting sensor trend."""
    trend = get_sensor_trend("EQ-001", "SENSOR-VIB", days=7)
    assert isinstance(trend, list)


def test_get_equipment_trends():
    """Test getting equipment trends."""
    trends = get_equipment_trends("EQ-001", days=7)
    assert isinstance(trends, dict)


def test_get_equipment_status_distribution():
    """Test getting status distribution."""
    dist = get_equipment_status_distribution()
    assert isinstance(dist, dict)
    assert len(dist) > 0


def test_get_alert_frequency():
    """Test getting alert frequency."""
    freq = get_alert_frequency(days=30)
    assert isinstance(freq, list)


def test_get_maintenance_status_distribution():
    """Test getting maintenance status."""
    dist = get_maintenance_status_distribution()
    assert isinstance(dist, dict)


def test_get_data_completeness():
    """Test getting data completeness."""
    stats = get_data_completeness()
    assert "total_equipment" in stats
    assert "total_mappings" in stats
    assert "total_readings" in stats
    assert stats["total_equipment"] >= 15


def test_get_summary_stats():
    """Test getting summary stats."""
    stats = get_summary_stats()
    assert "total_equipment" in stats
    assert "total_readings" in stats
    assert "open_alerts" in stats
    assert "open_work_orders" in stats