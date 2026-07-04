from uuid import uuid4
from .registry import JsonRegistry
from .config import DATA_PATH
from .models import Task


class TaskManager:
    def __init__(self):
        self.registry = JsonRegistry(DATA_PATH / "tasks.json")

    def create(self, title: str, agent: str):
        task = Task(id=str(uuid4()), title=title, agent=agent)
        data = self.registry.read()
        data[task.id] = task.model_dump(mode="json")
        self.registry.write(data)
        return task.model_dump(mode="json")

    def list(self):
        return self.registry.list()
