# RamaBJP — Predictive Maintenance for Defence Equipment

**PROOF OF CONCEPT | SYNTHETIC DEMO DATA | RULE-BASED LOGIC | NO LIVE SENSOR CONNECTION**

---

## 1. Project Purpose

RamaBJP is a software Proof of Concept built for the **Seva First Innovation Challenge 2026 (Maharashtra Zone)**. It demonstrates how a maintenance dashboard could display equipment condition, simulated readings, and rule-based warnings in a Defence MRO context.

**Target Sector:** Defence MRO (Maintenance, Repair and Overhaul)

---

## 2. Current Implemented Capabilities

| Module | Features |
| :--- | :--- |
| **Dashboard** | Summary metrics, status distribution, recent alerts |
| **Equipment** | View, add, edit, delete, search, filter |
| **Sensors** | 8 sensor types, equipment-sensor mapping, live status |
| **Alerts** | Alert list, acknowledge, resolve, filter |
| **Maintenance** | Work orders, create, assign, complete |
| **Analytics** | Status distribution, maintenance trends, data completeness |
| **Research** | Predictive vs preventive vs reactive maintenance |
| **Roadmap** | 6-phase implementation plan |
| **Ideas** | 10 future features |

---

## 3. Explicit Limitations

- **Synthetic demo data only** — not real equipment readings
- **Rule-based logic** — NOT AI/ML
- **No live sensor connection** — data is simulated
- **Thresholds are illustrative** — not official specifications
- **Failure prediction is NOT validated** — 12-15 days is illustrative only
- **Not field-tested** — no real-world deployment yet

---

## 4. Technology Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.12.10 |
| **UI Framework** | Streamlit 1.65.0 |
| **Data Processing** | pandas 3.0.6 |
| **Numerical** | NumPy 2.5.4 |
| **Visualization** | Plotly 7.1.0 |
| **Testing** | pytest 8.3.4 |
| **Database** | SQLite (built-in) |
| **Authentication** | passlib 1.7.4, bcrypt 4.2.1 |
| **Environment** | python-dotenv 1.0.1 |

---

## 5. Project Folder Structure
RamaBJP/
├── app.py # Main entry point
├── requirements.txt # Dependencies
├── README.md # This file
├── .gitignore # Git ignore rules
├── .env.example # Environment template
├── run_windows.bat # Windows launcher
├── cleanup.py # Cleanup script
├── analytics/ # Analytics module
│ ├── init.py
│ └── trends.py
├── components/ # UI components
│ ├── init.py
│ └── sidebar.py
├── config/ # Configuration
│ ├── init.py
│ └── theme.py
├── data/ # Database files
│ └── ramabjp.db
├── database/ # Database layer
│ ├── init.py
│ ├── db.py
│ ├── schema.sql
│ ├── seed.py
│ └── check_db.py
├── docs/ # Documentation
│ ├── architecture.md
│ ├── data_schema.md
│ ├── security.md
│ └── testing.md
├── domain/ # Domain models
│ └── init.py
├── ingestion/ # Data ingestion
│ └── init.py
├── pages/ # Streamlit pages
│ ├── init.py
│ ├── dashboard.py
│ ├── equipment.py
│ ├── sensors.py
│ ├── alerts.py
│ ├── maintenance.py
│ ├── analytics.py
│ ├── research.py
│ ├── roadmap.py
│ └── ideas.py
├── repositories/ # Data access layer
│ ├── init.py
│ ├── equipment_repo.py
│ ├── sensor_repo.py
│ ├── alert_repo.py
│ └── maintenance_repo.py
├── rules/ # Rule engine
│ ├── init.py
│ └── engine.py
├── security/ # Security (future)
│ └── init.py
├── services/ # Services (future)
│ └── init.py
└── tests/ # Tests
├── init.py
├── test_equipment.py
├── test_sensors.py
├── test_rules.py
├── test_alerts.py
├── test_maintenance.py
└── test_analytics.py


---

## 6. Python Installation Requirements

- **Python 3.12.10** (or compatible 3.12.x)
- **Windows 10** (or Windows 11)

---

## 7. Windows Setup Instructions

### Step 1: Install Python 3.12

Download from [python.org](https://www.python.org/downloads/) and install. **Important:** Tick "Add Python to PATH".

### Step 2: Open PowerShell in Project Folder

```powershell
cd C:\Users\PC\Desktop\RamaBJP