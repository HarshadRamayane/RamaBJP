# RamaBJP — Data Schema

## Tables

### 1. equipment

| Column | Type | Description |
| :--- | :--- | :--- |
| equipment_id | TEXT (PK) | Unique ID |
| name | TEXT | Equipment name |
| category | TEXT | Category |
| manufacturer | TEXT | Manufacturer |
| model | TEXT | Model |
| location | TEXT | Location |
| installation_date | TEXT | Installation date |
| last_maintenance_date | TEXT | Last maintenance |
| next_maintenance_date | TEXT | Next maintenance |
| status | TEXT | Normal/Warning/Critical |
| notes | TEXT | Notes |
| created_at | TEXT | Created timestamp |
| updated_at | TEXT | Updated timestamp |

### 2. sensor_definitions

| Column | Type | Description |
| :--- | :--- | :--- |
| sensor_id | TEXT (PK) | Unique ID |
| sensor_type | TEXT | Type (vibration, etc.) |
| name | TEXT | Sensor name |
| unit | TEXT | Measurement unit |
| description | TEXT | Description |

### 3. equipment_sensors

| Column | Type | Description |
| :--- | :--- | :--- |
| id | INTEGER (PK) | Auto ID |
| equipment_id | TEXT (FK) | Equipment ID |
| sensor_id | TEXT (FK) | Sensor ID |
| installed_at | TEXT | Install date |
| is_active | INTEGER | 1 = active |

### 4. sensor_readings

| Column | Type | Description |
| :--- | :--- | :--- |
| id | INTEGER (PK) | Auto ID |
| equipment_id | TEXT (FK) | Equipment ID |
| sensor_id | TEXT (FK) | Sensor ID |
| timestamp | TEXT | Reading time |
| value | REAL | Reading value |
| unit | TEXT | Unit |
| source | TEXT | DEMO/IMPORTED/LIVE |
| quality | TEXT | Good/Stale/Invalid |
| created_at | TEXT | Created timestamp |

### 5. rule_definitions

| Column | Type | Description |
| :--- | :--- | :--- |
| rule_id | TEXT (PK) | Unique ID |
| sensor_type | TEXT | Sensor type |
| unit | TEXT | Unit |
| warning_threshold | REAL | Warning level |
| critical_threshold | REAL | Critical level |
| comparison_direction | TEXT | greater_than / less_than |
| description | TEXT | Rule description |
| enabled | INTEGER | 1 = enabled |
| version | TEXT | Rule version |
| created_at | TEXT | Created timestamp |
| updated_at | TEXT | Updated timestamp |

### 6. alerts

| Column | Type | Description |
| :--- | :--- | :--- |
| alert_id | INTEGER (PK) | Auto ID |
| equipment_id | TEXT (FK) | Equipment ID |
| sensor_id | TEXT | Sensor ID |
| severity | TEXT | Critical/Warning |
| status | TEXT | OPEN/ACKNOWLEDGED/RESOLVED |
| message | TEXT | Alert message |
| reading_value | REAL | Reading value |
| threshold_value | REAL | Threshold |
| rule_id | TEXT | Rule ID |
| created_at | TEXT | Created timestamp |
| acknowledged_at | TEXT | Acknowledged timestamp |
| acknowledged_by | TEXT | User |
| resolved_at | TEXT | Resolved timestamp |
| resolved_by | TEXT | User |
| resolution_notes | TEXT | Notes |

### 7. work_orders

| Column | Type | Description |
| :--- | :--- | :--- |
| work_order_id | TEXT (PK) | Unique ID |
| equipment_id | TEXT (FK) | Equipment ID |
| issue | TEXT | Issue description |
| priority | TEXT | Low/Medium/High/Critical |
| status | TEXT | Open/In Progress/Completed |
| assigned_to | TEXT | Technician |
| planned_date | TEXT | Planned date |
| completed_date | TEXT | Completion date |
| work_performed | TEXT | Work done |
| parts_used | TEXT | Parts used |
| notes | TEXT | Notes |
| created_at | TEXT | Created timestamp |
| updated_at | TEXT | Updated timestamp |

### 8. audit_events

| Column | Type | Description |
| :--- | :--- | :--- |
| id | INTEGER (PK) | Auto ID |
| actor | TEXT | User |
| action | TEXT | Action type |
| entity_type | TEXT | Entity type |
| entity_id | TEXT | Entity ID |
| details | TEXT | Details |
| timestamp | TEXT | Timestamp |