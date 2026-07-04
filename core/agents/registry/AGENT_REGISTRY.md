# AI Enterprise OS — Agent Registry

## Core Principle

Each project is managed by a dedicated Hermes agent.

The terminal is used only for bootstrap and emergency maintenance. Normal project work should be performed by Hermes agents.

## Agents

| Agent | Hermes Profile | Workspace | Role |
|---|---|---|---|
| Architect | platform-admin | /opt/ai-enterprise-os | Platform administrator |
| H-Scraper Agent | hscraper | /opt/ai-enterprise-os/workspaces/hscraper | Scraping platform development |
| Odysseus Agent | odysseus | /opt/ai-enterprise-os/workspaces/odysseus | Deep research and strategic intelligence |
| Hospital AI Agent | hospital-ai | /opt/ai-enterprise-os/workspaces/hospital-ai | HIS, medical AI, healthcare systems |
| Automation Agent | automation | /opt/ai-enterprise-os/workspaces/automation | Scheduled jobs and background workflows |
| Research Lab Agent | research-lab | /opt/ai-enterprise-os/workspaces/research-lab | Experiments, model tests, evaluations |
| Sandbox Agent | sandbox | /opt/ai-enterprise-os/workspaces/sandbox | Safe testing and prototyping |
