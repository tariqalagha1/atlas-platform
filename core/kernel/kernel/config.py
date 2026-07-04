from pathlib import Path

BASE_PATH = Path("/opt/ai-enterprise-os")
CORE_PATH = BASE_PATH / "core"
WORKSPACES_PATH = BASE_PATH / "workspaces"
PROFILES_PATH = CORE_PATH / "profiles"
AGENTS_PATH = CORE_PATH / "agents"
KERNEL_PATH = CORE_PATH / "kernel"
DATA_PATH = KERNEL_PATH / "data"
LOGS_PATH = KERNEL_PATH / "logs"
