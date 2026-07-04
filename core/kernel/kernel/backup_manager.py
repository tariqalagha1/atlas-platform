from datetime import datetime
from .registry import JsonRegistry
from .config import DATA_PATH, BASE_PATH


class BackupManager:
    def __init__(self):
        self.registry = JsonRegistry(DATA_PATH / "backups.json")

    def register_snapshot(self, label: str):
        item = {
            "label": label,
            "base_path": str(BASE_PATH),
            "status": "registered",
            "created_at": datetime.utcnow().isoformat(),
        }
        data = self.registry.read()
        data[label] = item
        self.registry.write(data)
        return item

    def list(self):
        return self.registry.list()
