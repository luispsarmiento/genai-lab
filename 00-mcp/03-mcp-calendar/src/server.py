import json
import os
import uuid
from datetime import datetime
from typing import List, Optional
from mcp.server.fastmcp import FastMCP
from icalendar import Calendar, Event as ICalEvent

server = FastMCP("mcp-calendar")

# Storage path for calendar events (simple JSON file)
STORAGE_PATH = os.path.join(os.getcwd(), "calendar_events.json")

def load_events():
    if not os.path.exists(STORAGE_PATH):
        return []
    with open(STORAGE_PATH, "r") as f:
        return json.load(f)

def save_events(events):
    with open(STORAGE_PATH, "w") as f:
        json.dump(events, f, indent=4)

@server.tool(
    name="register_event",
    title="Register Event",
    description="Registers a new calendar event"
)
async def register_event(
    title: str,
    start_time: str,
    end_time: str,
    description: Optional[str] = "",
    location: Optional[str] = ""
) -> str:
    """Register a new calendar event.

    Args:
        title: Title of the event
        start_time: Start time in ISO 8601 format (YYYY-MM-DD HH:MM:SS or YYYY-MM-DDTHH:MM:SS)
        end_time: End time in ISO 8601 format
        description: Optional description of the event
        location: Optional location of the event
    """
    events = load_events()
    event_id = str(uuid.uuid4())
    
    # Simple validation/formatting
    try:
        # Convert to ISO format if it's not
        start_dt = datetime.fromisoformat(start_time.replace(" ", "T"))
        end_dt = datetime.fromisoformat(end_time.replace(" ", "T"))
    except ValueError as e:
        return f"Error: Invalid date format. Please use ISO 8601 format (e.g., 2023-10-27T10:00:00). Details: {str(e)}"

    new_event = {
        "id": event_id,
        "title": title,
        "start": start_dt.isoformat(),
        "end": end_dt.isoformat(),
        "description": description,
        "location": location
    }
    
    events.append(new_event)
    save_events(events)
    
    return f"Event registered successfully with ID: {event_id}"

@server.tool(
    name="list_events",
    title="List Events",
    description="Lists all registered calendar events"
)
async def list_events() -> str:
    """Lists all registered calendar events."""
    events = load_events()
    if not events:
        return "No events found."
    
    return json.dumps(events, indent=2)

@server.tool(
    name="get_ics_file",
    title="Get ICS File",
    description="Generates an ICS file content for a specific event ID"
)
async def get_ics_file(event_id: str) -> str:
    """Generates ICS content for an event.

    Args:
        event_id: The ID of the event to export
    """
    events = load_events()
    event = next((e for e in events if e["id"] == event_id), None)
    
    if not event:
        return f"Error: Event with ID {event_id} not found."
    
    cal = Calendar()
    cal.add('prodid', '-//MCP Calendar Server//mx//')
    cal.add('version', '2.0')
    
    ical_event = ICalEvent()
    ical_event.add('summary', event['title'])
    ical_event.add('dtstart', datetime.fromisoformat(event['start']))
    ical_event.add('dtend', datetime.fromisoformat(event['end']))
    if event['description']:
        ical_event.add('description', event['description'])
    if event['location']:
        ical_event.add('location', event['location'])
    ical_event.add('dtstamp', datetime.now())
    ical_event['uid'] = event['id']
    
    cal.add_component(ical_event)
    
    return cal.to_ical().decode("utf-8")
