# Hermes Profile Registry

## Purpose

Each project has its own Hermes profile, memory, skills, sessions, logs, and rules.

## Profiles

| Profile | Role | Workspace |
|---|---|---|
| platform-admin | Controls the whole AI Enterprise OS | /opt/ai-enterprise-os |
| hscraper | Manages H-Scraper project | /opt/ai-enterprise-os/workspaces/hscraper |
| odysseus | Deep search and strategic intelligence | /opt/ai-enterprise-os/workspaces/odysseus |
| hospital-ai | Healthcare/HIS/medical AI projects | /opt/ai-enterprise-os/workspaces/hospital-ai |
| automation | Scheduled jobs and background agents | /opt/ai-enterprise-os/workspaces/automation |
| research-lab | Experiments, models, evaluations | /opt/ai-enterprise-os/workspaces/research-lab |
| sandbox | Safe testing area | /opt/ai-enterprise-os/workspaces/sandbox |

## Rule

No profile should modify another workspace unless explicitly authorized.
