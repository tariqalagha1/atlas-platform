from .registry import JsonRegistry
from .config import DATA_PATH


class CapabilityEngine:
    def __init__(self):
        self.registry = JsonRegistry(DATA_PATH / "capabilities.json")

    def bootstrap(self):
        capabilities = {
            "platform-administration": {
                "primary_agent": "platform-admin",
                "agents": ["platform-admin"],
                "description": "Manage the AI Enterprise OS platform"
            },
            "web-scraping": {
                "primary_agent": "hscraper",
                "agents": ["hscraper"],
                "description": "Scraping, crawling, extraction, anti-bot workflows"
            },
            "deep-research": {
                "primary_agent": "odysseus",
                "agents": ["odysseus"],
                "description": "Deep search, evidence collection, strategic intelligence"
            },
            "medical-ai": {
                "primary_agent": "hospital-ai",
                "agents": ["hospital-ai"],
                "description": "Healthcare, HIS, RIS, LIS, PMS, PACS, ICD, clinical workflows"
            },
            "automation": {
                "primary_agent": "automation",
                "agents": ["automation"],
                "description": "Scheduled tasks, background jobs, workflow automation"
            },
            "experimentation": {
                "primary_agent": "research-lab",
                "agents": ["research-lab", "sandbox"],
                "description": "Model tests, experiments, prototypes, evaluations"
            },
            "safe-prototyping": {
                "primary_agent": "sandbox",
                "agents": ["sandbox"],
                "description": "Low-risk testing before production"
            }
        }
        self.registry.write(capabilities)
        return capabilities

    def list(self):
        return self.registry.list()

    def route(self, capability: str):
        data = self.registry.read()
        if capability not in data:
            return {
                "status": "not_found",
                "capability": capability,
                "message": "Capability is not registered"
            }

        item = data[capability]
        return {
            "status": "routed",
            "capability": capability,
            "primary_agent": item["primary_agent"],
            "available_agents": item["agents"],
            "description": item["description"]
        }
