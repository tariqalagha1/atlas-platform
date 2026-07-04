from .registry import JsonRegistry
from .config import DATA_PATH


class DependencyManager:
    def __init__(self):
        self.registry = JsonRegistry(DATA_PATH / "dependencies.json")

    def bootstrap(self):
        graph = {
            "platform-admin": ["kernel", "profiles", "agents"],
            "hscraper": ["web-scraping", "docker", "python"],
            "odysseus": ["deep-research", "knowledge", "model-router"],
            "hospital-ai": ["medical-ai", "knowledge", "model-router"],
            "automation": ["scheduler", "events", "tasks"],
            "research-lab": ["models", "experiments", "sandbox"],
            "sandbox": ["isolated-workspace"]
        }
        self.registry.write(graph)
        return graph

    def list(self):
        return self.registry.list()
