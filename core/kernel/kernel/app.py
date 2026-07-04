from fastapi import FastAPI
from .workspace_manager import WorkspaceManager
from .agent_manager import AgentManager
from .service_manager import ServiceManager
from .model_router import ModelRouter
from .memory_manager import MemoryManager
from .task_manager import TaskManager
from .events import EventBus
from .backup_manager import BackupManager
from .capability_engine import CapabilityEngine
from .dependency_manager import DependencyManager

app = FastAPI(title="AI Enterprise OS Kernel", version="0.1.0")

workspace_manager = WorkspaceManager()
agent_manager = AgentManager()
service_manager = ServiceManager()
model_router = ModelRouter()
memory_manager = MemoryManager()
task_manager = TaskManager()
event_bus = EventBus()
backup_manager = BackupManager()
capability_engine = CapabilityEngine()
dependency_manager = DependencyManager()


@app.get("/")
def root():
    return {
        "name": "AI Enterprise OS Kernel",
        "version": "0.1.0",
        "status": "online",
    }


@app.post("/bootstrap")
def bootstrap():
    return {
        "workspaces": workspace_manager.discover(),
        "agents": agent_manager.discover(),
        "services": service_manager.bootstrap(),
        "models": model_router.bootstrap(),
        "memory": memory_manager.bootstrap(),
        "backup": backup_manager.register_snapshot("pk-0001-bootstrap"),
        "capabilities": capability_engine.bootstrap(),
        "dependencies": dependency_manager.bootstrap(),
        "event": event_bus.publish("kernel", "bootstrap.complete", {"version": "0.1.0"}),
    }


@app.get("/workspaces")
def list_workspaces():
    return workspace_manager.list()


@app.get("/agents")
def list_agents():
    return agent_manager.list()


@app.get("/services")
def list_services():
    return service_manager.list()


@app.get("/models")
def list_models():
    return model_router.list()


@app.get("/memory")
def list_memory():
    return memory_manager.list()


@app.post("/tasks")
def create_task(title: str, agent: str):
    return task_manager.create(title=title, agent=agent)


@app.get("/tasks")
def list_tasks():
    return task_manager.list()


@app.post("/events")
def publish_event(source: str, event_type: str):
    return event_bus.publish(source=source, event_type=event_type)


@app.get("/events")
def list_events():
    return event_bus.list()


@app.get("/backups")
def list_backups():
    return backup_manager.list()


@app.get("/capabilities")
def list_capabilities():
    return capability_engine.list()


@app.get("/capabilities/route/{capability}")
def route_capability(capability: str):
    return capability_engine.route(capability)


@app.get("/dependencies")
def list_dependencies():
    return dependency_manager.list()
