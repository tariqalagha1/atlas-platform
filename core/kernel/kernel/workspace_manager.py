from pathlib import Path
from .config import WORKSPACES_PATH
from .registry import JsonRegistry
from .models import Workspace


class WorkspaceManager:
    def __init__(self):
        self.registry = JsonRegistry(WORKSPACES_PATH.parent / "kernel" / "data" / "workspaces.json")

    def discover(self):
        result = {}
        for path in WORKSPACES_PATH.iterdir():
            if path.is_dir():
                ws = Workspace(name=path.name, path=str(path))
                result[path.name] = ws.model_dump()
        self.registry.write(result)
        return result

    def list(self):
        return self.registry.list()

    def create(self, name: str, description: str = ""):
        path = WORKSPACES_PATH / name
        path.mkdir(parents=True, exist_ok=True)
        for folder in ["project", "docs", "data", "logs", "config", "tasks", "outputs"]:
            (path / folder).mkdir(exist_ok=True)

        ws = Workspace(name=name, path=str(path), description=description)
        self.registry.set(name, ws.model_dump())
        return ws.model_dump()
