from datetime import datetime, UTC
from uuid import uuid4


class EventBus:

    def __init__(self):
        self.events = []

    def publish(self, source, event_type, payload=None):

        event = {
            "id": str(uuid4()),
            "source": source,
            "type": event_type,
            "payload": payload or {},
            "created_at": datetime.now(UTC).isoformat(),
        }

        self.events.append(event)

        return event

    def list_events(self):
        return self.events
