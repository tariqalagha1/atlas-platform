# AI Enterprise OS — VPS Platform Map

## Existing Projects

- `/opt/scraper-deploy`
  - Existing H-Scraper project
  - Must not be modified without explicit approval

## New Platform

- `/opt/ai-enterprise-os`

### Core

- `core/hermes`
- `core/profiles`
- `core/skills`
- `core/memory`
- `core/model-router`
- `core/gateway`
- `core/dashboard`
- `core/governance`

### Workspaces

- `workspaces/hscraper`
- `workspaces/odysseus`
- `workspaces/hospital-ai`
- `workspaces/automation`
- `workspaces/research-lab`
- `workspaces/sandbox`

### Shared Services

- `shared/postgres`
- `shared/redis`
- `shared/qdrant`
- `shared/minio`
- `shared/nginx`
- `shared/monitoring`

### Storage

- `storage/datasets`
- `storage/models`
- `storage/exports`
- `storage/knowledge`
- `storage/archives`
