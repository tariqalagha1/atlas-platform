from uuid import uuid4
from .registry import JsonRegistry
from .config import DATA_PATH
from .models import Event


class EventBus:
    def __init__(self):
        self.registry = JsonRegistry(DATA_PATH / "events.json")

    def publish(self, source: str, event_type: str, payload: dict = None):
        event = Event(
            id=str(uuid4()),
            source=source,
            type=event_type,
            payload=payload or {},
        )
        data = self.registry.read()
        data[event.id] = event.model_dump(mode="json")
        self.registry.write(data)
        return event.model_dump(mode="json")

    def list(self):
        return self.registry.list()
