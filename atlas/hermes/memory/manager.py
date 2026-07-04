import json
from pathlib import Path


class MemoryManager:

    def __init__(self, workspace: str):

        self.workspace = workspace

        self.memory_dir = (
            Path("/opt/ai-enterprise-os")
            / "workspaces"
            / workspace
            / "memory"
        )

        self.memory_dir.mkdir(parents=True, exist_ok=True)

        self.memory_file = self.memory_dir / "memory.json"

    def load(self):

        if not self.memory_file.exists():
            self.save(
                {
                    "knowledge": [],
                    "skills": [],
                    "architecture": [],
                }
            )

        with open(self.memory_file) as f:
            return json.load(f)

    def save(self, memory):

        with open(self.memory_file, "w") as f:
            json.dump(memory, f, indent=2)
