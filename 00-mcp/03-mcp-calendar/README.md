# MCP Calendar Server

A Model Context Protocol (MCP) server that allows registering, listing, and exporting calendar events.

## Features

1.  **Register events:** Register new calendar events with title, start/end time, description, and location.
2.  **List events:** View all registered events.
3.  **Export to ICS:** Get the ICS file content for an event to import into Google Calendar, Outlook, etc.

## Installation

```bash
pip install mcp icalendar
```

## Tools

- `register_event`: Registers a new event.
    - `title` (string): Event title.
    - `start_time` (string): Start time (ISO 8601).
    - `end_time` (string): End time (ISO 8601).
    - `description` (string, optional): Event description.
    - `location` (string, optional): Event location.
- `list_events`: Lists all events.
- `get_ics_file`: Returns ICS content for a given `event_id`.

## Usage

### Running the server

```bash
python src/app.py
```

By default, it uses `stdio` transport. You can change it via environment variables:

```bash
$env:TRANSPORT="streamable-http"
python src/app.py
```
