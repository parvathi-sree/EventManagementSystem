# 🗓️ Mini Event Management System API

A Flask-based backend system for managing events and attendee registrations. Built with clean architecture, PostgreSQL, and Swagger documentation.

---

## Features

- Create and list events
- Register attendees (with duplicate and capacity checks)
- View attendee lists per event
- Pagination support for attendee list
- Timezone-aware event handling (default: IST)
- API documentation with Swagger (via YAML)
- PostgreSQL + SQLAlchemy + Flask-Migrate
- Unit tests using pytest

---

## Requirements

- Python 3.10+
- Flask
- SQLAlchemy
- PostgreSQL
- Flask-Migrate
- Flasgger (Swagger UI)
- pytest

---

##  Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/user-name/EventManagementSystem.git
cd EventManagementSystem
