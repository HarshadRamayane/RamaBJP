"""
Tests for sensor repository.
"""

import pytest
from repositories.sensor_repo import (
    get_all_sensor_definitions, get_sensor_by_id, get_sensor_by_type,
    get_sensors_for_equipment, get_equipment_for_sensor,
    add_reading, get_latest_reading, get_readings_for_equipment,
    get_sensor_stats
)


def test_get_all_sensor_definitions():
    """Test getting all sensor definitions."""
    sensors = get_all_sensor_definitions()
    assert len(sensors) == 8


def test_get_sensor_by_id():
    """Test getting sensor by ID."""
    sensor = get_sensor_by_id("SENSOR-VIB")
    assert sensor is not None
    assert sensor["sensor_type"] == "vibration"


def test_get_sensor_by_type():
    """Test getting sensor by type."""
    sensor = get_sensor_by_type("temperature")
    assert sensor is not None
    assert sensor["unit"] == "°C"


def test_get_sensors_for_equipment():
    """Test getting sensors for an equipment."""
    sensors = get_sensors_for_equipment("EQ-001")
    assert len(sensors) > 0


def test_get_equipment_for_sensor():
    """Test getting equipment for a sensor."""
    equipment = get_equipment_for_sensor("SENSOR-VIB")
    assert len(equipment) > 0


def test_add_reading():
    """Test adding a sensor reading."""
    reading_id = add_reading("EQ-001", "SENSOR-VIB", 0.5, "RMS", "DEMO")
    assert reading_id is not None


def test_get_latest_reading():
    """Test getting latest reading."""
    add_reading("EQ-001", "SENSOR-TEMP", 65.5, "°C", "DEMO")
    reading = get_latest_reading("EQ-001", "SENSOR-TEMP")
    assert reading is not None
    assert reading["value"] == 65.5


def test_get_readings_for_equipment():
    """Test getting readings for equipment."""
    readings = get_readings_for_equipment("EQ-001")
    assert len(readings) > 0


def test_get_sensor_stats():
    """Test sensor statistics."""
    stats = get_sensor_stats()
    assert stats["total_sensors"] == 8
    assert stats["total_mappings"] > 0
    assert stats["total_readings"] > 0