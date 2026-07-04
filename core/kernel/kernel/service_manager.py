from .registry import JsonRegistry
from .config import DATA_PATH
from .models import Service


class ServiceManager:
    def __init__(self):
        self.registry = JsonRegistry(DATA_PATH / "services.json")

    def bootstrap(self):
        services = {
            "hermes": Service(name="hermes", type="agent-runtime", status="planned").model_dump(),
            "postgres": Service(name="postgres", type="database", status="planned", port=5432).model_dump(),
            "redis": Service(name="redis", type="cache", status="planned", port=6379).model_dump(),
            "qdrant": Service(name="qdrant", type="vector-db", status="planned", port=6333).model_dump(),
            "minio": Service(name="minio", type="object-storage", status="planned", port=9000).model_dump(),
            "nginx": Service(name="nginx", type="reverse-proxy", status="planned", port=80).model_dump(),
        }
        self.registry.write(services)
        return services

    def list(self):
        return self.registry.list()
