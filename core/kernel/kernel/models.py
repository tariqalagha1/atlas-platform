from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime


class Workspace(BaseModel):
    name: str
    path: str
    status: str = "created"
    description: Optional[str] = None


class Agent(BaseModel):
    name: str
    profile: str
    workspace: str
    role: str
    status: str = "draft"
    capabilities: List[str] = []


class Service(BaseModel):
    name: str
    type: str
    status: str = "unknown"
    port: Optional[int] = None


class Task(BaseModel):
    id: str
    title: str
    agent: str
    status: str = "queued"
    created_at: datetime = datetime.utcnow()


class Event(BaseModel):
    id: str
    source: str
    type: str
    payload: Dict = {}
    created_at: datetime = datetime.utcnow()
