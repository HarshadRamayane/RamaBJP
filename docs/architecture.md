# RamaBJP — Architecture

## Overview

RamaBJP is a modular Python application built with Streamlit. It follows a layered architecture with clear separation of concerns.

## Layers
┌─────────────────────────────────────────┐
│ Presentation Layer │
│ (pages/, components/) │
├─────────────────────────────────────────┤
│ Business Logic Layer │
│ (rules/, analytics/) │
├─────────────────────────────────────────┤
│ Service Layer │
│ (services/) │
├─────────────────────────────────────────┤
│ Repository Layer │
│ (repositories/) │
├─────────────────────────────────────────┤
│ Database Layer │
│ (database/) │
└─────────────────────────────────────────┘

## Modules

| Layer | Module | Purpose |
| :--- | :--- | :--- |
| Presentation | `pages/` | Streamlit UI pages |
| Presentation | `components/` | Reusable UI components |
| Business | `rules/` | Rule engine |
| Business | `analytics/` | Trend analysis |
| Repository | `repositories/` | Data access |
| Database | `database/` | SQLite operations |
| Config | `config/` | Theme, settings |

## Data Flow
User → Streamlit UI → Service → Repository → SQLite
↓
Rule Engine → Alert Creation
↓
Analytics → Charts


## Key Design Decisions

1. **SQLite** — Simple, local, no server needed
2. **Rule-based logic** — Transparent, no AI/ML needed
3. **Synthetic data** — Safe for demonstration
4. **Modular structure** — Easy to maintain and extend
5. **White theme** — Professional, accessible