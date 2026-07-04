import json
from pathlib import Path
from datetime import datetime, UTC


class SessionManager:

    def __init__(self, workspace: str):
        self.workspace = workspace

        self.session_dir = (
            Path("/opt/ai-enterprise-os")
            / "workspaces"
            / workspace
            / "session"
        )

        self.session_dir.mkdir(parents=True, exist_ok=True)

        self.session_file = self.session_dir / "current.json"

    def load(self):

        if not self.session_file.exists():
            return None

        with open(self.session_file, "r") as f:
            return json.load(f)

    def save(self, data: dict):

        data["updated_at"] = datetime.now(UTC).isoformat()

        with open(self.session_file, "w") as f:
            json.dump(data, f, indent=2)

        return data

    def bootstrap(self):

        session = self.load()

        if session:
            return session

        session = {
            "workspace": self.workspace,
            "status": "new",
            "tasks": [],
            "decisions": [],
            "conversation": [],
        }

        return self.save(session)
