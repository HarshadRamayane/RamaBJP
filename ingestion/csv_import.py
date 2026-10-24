"""
RamaBJP CSV Import Module
Handles CSV file upload and validation for sensor readings.
"""

import pandas as pd
from io import StringIO
from database.db import get_connection, now_iso


# Maximum allowed rows
MAX_ROWS = 10000

# Required columns
REQUIRED_COLUMNS = ["equipment_id", "sensor_id", "timestamp", "value", "unit"]


def validate_csv_schema(df):
    """Validate that CSV has all required columns."""
    errors = []
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        errors.append(f"Missing required columns: {', '.join(missing)}")
    return errors


def validate_csv_data(df):
    """Validate the data in the CSV."""
    errors = []
    
    # Check row count
    if len(df) == 0:
        errors.append("CSV file is empty")
        return errors
    
    if len(df) > MAX_ROWS:
        errors.append(f"Too many rows ({len(df)}). Maximum: {MAX_ROWS}")
        return errors
    
    # Check for NaN in required fields
    for col in REQUIRED_COLUMNS:
        if df[col].isna().any():
            count = df[col].isna().sum()
            errors.append(f"Column '{col}' has {count} missing values")
    
    # Check numeric values
    try:
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        if df["value"].isna().any():
            errors.append("Column 'value' has non-numeric values")
    except Exception as e:
        errors.append(f"Error processing 'value' column: {e}")
    
    return errors


def preview_csv(df, limit=10):
    """Preview first N rows of the CSV."""
    return df.head(limit).to_dict("records")


def import_readings(df, source="IMPORTED"):
    """Import validated readings into the database."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        now = now_iso()
        
        imported = 0
        rejected = 0
        rejection_reasons = []
        
        for idx, row in df.iterrows():
            try:
                equipment_id = str(row["equipment_id"]).strip()
                sensor_id = str(row["sensor_id"]).strip()
                timestamp = str(row["timestamp"]).strip()
                value = float(row["value"])
                unit = str(row["unit"]).strip()
                
                # Verify equipment exists
                cursor.execute(
                    "SELECT 1 FROM equipment WHERE equipment_id = ?",
                    (equipment_id,)
                )
                if not cursor.fetchone():
                    rejected += 1
                    rejection_reasons.append(f"Row {idx+2}: Equipment {equipment_id} not found")
                    continue
                
                # Verify sensor exists
                cursor.execute(
                    "SELECT 1 FROM sensor_definitions WHERE sensor_id = ?",
                    (sensor_id,)
                )
                if not cursor.fetchone():
                    rejected += 1
                    rejection_reasons.append(f"Row {idx+2}: Sensor {sensor_id} not found")
                    continue
                
                # Insert reading
                cursor.execute("""
                    INSERT INTO sensor_readings 
                    (equipment_id, sensor_id, timestamp, value, unit, source, quality, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, 'Good', ?)
                """, (equipment_id, sensor_id, timestamp, value, unit, source, now))
                imported += 1
                
            except Exception as e:
                rejected += 1
                rejection_reasons.append(f"Row {idx+2}: {str(e)}")
        
        conn.commit()
        
        return {
            "imported": imported,
            "rejected": rejected,
            "reasons": rejection_reasons[:20]  # limit to 20
        }
    finally:
        conn.close()


def generate_sample_csv():
    """Generate a sample CSV template."""
    from datetime import datetime, timedelta
    
    now = datetime.now()
    data = {
        "equipment_id": ["EQ-001", "EQ-001", "EQ-002", "EQ-002", "EQ-003"],
        "sensor_id": ["SENSOR-VIB", "SENSOR-TEMP", "SENSOR-VIB", "SENSOR-TEMP", "SENSOR-VIB"],
        "timestamp": [
            (now - timedelta(hours=i)).isoformat()
            for i in range(5)
        ],
        "value": [0.45, 65.2, 0.38, 62.1, 0.71],
        "unit": ["RMS", "°C", "RMS", "°C", "RMS"]
    }
    return pd.DataFrame(data)