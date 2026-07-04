from .config import AGENTS_PATH, PROFILES_PATH
from .registry import JsonRegistry
from .models import Agent


class AgentManager:
    def __init__(self):
        self.registry = JsonRegistry(AGENTS_PATH / "registry" / "agents.json")

    def discover(self):
        agents = {}
        profile_roles = {
            "platform-admin": ("Architect", "Controls the AI Enterprise OS platform", ["platform-admin"]),
            "hscraper": ("H-Scraper Agent", "Develops and manages H-Scraper", ["scraping", "coding"]),
            "odysseus": ("Odysseus Agent", "Deep research and strategic intelligence", ["deep-research", "analysis"]),
            "hospital-ai": ("Hospital AI Agent", "Healthcare AI systems", ["medical-ai", "his"]),
            "automation": ("Automation Agent", "Automation workflows", ["automation", "scheduler"]),
            "research-lab": ("Research Lab Agent", "Experiments and evaluations", ["experiments", "evaluation"]),
            "sandbox": ("Sandbox Agent", "Safe testing", ["prototype", "testing"]),
        }

        for profile, values in profile_roles.items():
            if (PROFILES_PATH / profile).exists():
                name, role, capabilities = values
                agent = Agent(
                    name=name,
                    profile=profile,
                    workspace=profile if profile != "platform-admin" else "platform",
                    role=role,
                    capabilities=capabilities,
                )
                agents[profile] = agent.model_dump()

        self.registry.write(agents)
        return agents

    def list(self):
        return self.registry.list()
