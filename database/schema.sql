-- ============================================================
-- RamaBJP Database Schema
-- Predictive Maintenance for Defence Equipment
-- ============================================================

-- Equipment Table
CREATE TABLE IF NOT EXISTS equipment (
    equipment_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    manufacturer TEXT,
    model TEXT,
    location TEXT,
    installation_date TEXT,
    last_maintenance_date TEXT,
    next_maintenance_date TEXT,
    status TEXT DEFAULT 'Unknown',
    notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

-- Sensor Definitions Table
CREATE TABLE IF NOT EXISTS sensor_definitions (
    sensor_id TEXT PRIMARY KEY,
    sensor_type TEXT NOT NULL,
    name TEXT NOT NULL,
    unit TEXT NOT NULL,
    description TEXT
);

-- Equipment-Sensor Mapping Table
CREATE TABLE IF NOT EXISTS equipment_sensors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id TEXT NOT NULL,
    sensor_id TEXT NOT NULL,
    installed_at TEXT NOT NULL,
    is_active INTEGER DEFAULT 1,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    FOREIGN KEY (sensor_id) REFERENCES sensor_definitions(sensor_id)
);

-- Sensor Readings Table
CREATE TABLE IF NOT EXISTS sensor_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id TEXT NOT NULL,
    sensor_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    value REAL NOT NULL,
    unit TEXT NOT NULL,
    source TEXT DEFAULT 'DEMO',
    quality TEXT DEFAULT 'Good',
    created_at TEXT NOT NULL,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    FOREIGN KEY (sensor_id) REFERENCES sensor_definitions(sensor_id)
);

-- Rule Definitions Table
CREATE TABLE IF NOT EXISTS rule_definitions (
    rule_id TEXT PRIMARY KEY,
    sensor_type TEXT NOT NULL,
    unit TEXT NOT NULL,
    warning_threshold REAL,
    critical_threshold REAL,
    comparison_direction TEXT DEFAULT 'greater_than',
    description TEXT,
    enabled INTEGER DEFAULT 1,
    version TEXT DEFAULT '1.0',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

-- Alerts Table
CREATE TABLE IF NOT EXISTS alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id TEXT NOT NULL,
    sensor_id TEXT,
    severity TEXT NOT NULL,
    status TEXT DEFAULT 'OPEN',
    message TEXT NOT NULL,
    reading_value REAL,
    threshold_value REAL,
    rule_id TEXT,
    created_at TEXT NOT NULL,
    acknowledged_at TEXT,
    acknowledged_by TEXT,
    resolved_at TEXT,
    resolved_by TEXT,
    resolution_notes TEXT,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Maintenance Work Orders Table
CREATE TABLE IF NOT EXISTS work_orders (
    work_order_id TEXT PRIMARY KEY,
    equipment_id TEXT NOT NULL,
    issue TEXT NOT NULL,
    priority TEXT DEFAULT 'Medium',
    status TEXT DEFAULT 'Open',
    assigned_to TEXT,
    planned_date TEXT,
    completed_date TEXT,
    work_performed TEXT,
    parts_used TEXT,
    notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id)
);

-- Audit Events Table
CREATE TABLE IF NOT EXISTS audit_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    actor TEXT,
    action TEXT NOT NULL,
    entity_type TEXT,
    entity_id TEXT,
    details TEXT,
    timestamp TEXT NOT NULL
);

-- ============================================================
-- INDEXES
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_readings_equipment ON sensor_readings(equipment_id);
CREATE INDEX IF NOT EXISTS idx_readings_timestamp ON sensor_readings(timestamp);
CREATE INDEX IF NOT EXISTS idx_alerts_equipment ON alerts(equipment_id);
CREATE INDEX IF NOT EXISTS idx_alerts_status ON alerts(status);
CREATE INDEX IF NOT EXISTS idx_workorders_equipment ON work_orders(equipment_id);