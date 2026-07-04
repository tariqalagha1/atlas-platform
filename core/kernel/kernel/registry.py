import json
from pathlib import Path
from typing import Any


class JsonRegistry:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.write({})

    def read(self) -> dict:
        return json.loads(self.path.read_text())

    def write(self, data: dict) -> None:
        self.path.write_text(json.dumps(data, indent=2))

    def set(self, key: str, value: Any) -> None:
        data = self.read()
        data[key] = value
        self.write(data)

    def get(self, key: str, default=None):
        return self.read().get(key, default)

    def list(self) -> dict:
        return self.read()
