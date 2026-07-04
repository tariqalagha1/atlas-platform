from .registry import JsonRegistry
from .config import DATA_PATH


class MemoryManager:
    def __init__(self):
        self.registry = JsonRegistry(DATA_PATH / "memory.json")

    def bootstrap(self):
        memory = {
            "global": {"type": "shared", "status": "planned"},
            "platform-admin": {"type": "private", "status": "created"},
            "hscraper": {"type": "private", "status": "created"},
            "odysseus": {"type": "private", "status": "created"},
            "hospital-ai": {"type": "private", "status": "created"},
            "automation": {"type": "private", "status": "created"},
            "research-lab": {"type": "private", "status": "created"},
            "sandbox": {"type": "private", "status": "created"},
        }
        self.registry.write(memory)
        return memory

    def list(self):
        return self.registry.list()
