from pathlib import Path

from atlas.hermes.session.manager import SessionManager
from atlas.hermes.memory.manager import MemoryManager


class HermesRuntime:

    def __init__(self, workspace: str):
        self.workspace = workspace
        self.base_path = Path("/opt/ai-enterprise-os")
        self.workspace_path = self.base_path / "workspaces" / workspace

    def start(self):

        if not self.workspace_path.exists():
            return {
                "status": "error",
                "workspace": self.workspace,
                "message": "Workspace not found"
            }

        session = SessionManager(self.workspace).bootstrap()
        memory = MemoryManager(self.workspace).load()

        return {
            "runtime": "hermes",
            "version": "0.2.0",
            "status": "ready",
            "workspace": self.workspace,
            "memory": "loaded",
            "session": session["status"],
            "memory_items": len(memory)
        }
