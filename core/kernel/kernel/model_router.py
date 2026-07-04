from .registry import JsonRegistry
from .config import DATA_PATH


class ModelRouter:
    def __init__(self):
        self.registry = JsonRegistry(DATA_PATH / "model_router.json")

    def bootstrap(self):
        routes = {
            "deep-research": {"preferred": "glm", "fallback": ["qwen", "openai"]},
            "coding": {"preferred": "qwen", "fallback": ["openai", "glm"]},
            "fast-extraction": {"preferred": "qwen", "fallback": ["glm"]},
            "medical-ai": {"preferred": "openai", "fallback": ["qwen"]},
            "automation": {"preferred": "qwen", "fallback": ["glm"]},
        }
        self.registry.write(routes)
        return routes

    def list(self):
        return self.registry.list()
