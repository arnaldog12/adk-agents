# adk-agents

## Setup

```sh
uv sync
source .venv/bin/activate
cp .env.example .env

gcloud auth login
gcloud config set project ${GOOGLE_CLOUD_PROJECT}
# enable vertexai and storage api

### 1. Start the Database and Toolbox Services

```bash
docker-compose up -d

This starts:
- PostgreSQL database on port 5432
- Google Database Toolbox on port 5001 (port 5000 conflicts with macOS AirPlay)

### 2. Set Environment Variables

Change the environment variables in the `.env` file to your own.

## Running


```bash
dk web --session_service_uri "sqlite:///./google_adk_agents.db" --memory_service_uri "agentengine://3732274628299587584"
```

### Level 1 (Agent + Tools + MCP - NL2SQL)

### Level 2 (Session + Memory + callbacks)

```bash
adk web levels --session_service_uri "sqlite:///./google_adk_agents.db" --memory_service_uri "agentengine://3732274628299587584"
```
### Level 3 (Knowledge + RAG + Reasoning)


### Level 4 (Multi-Agents)


### Level 5 (Workflow Agents)

## Troubleshooting

If you encounter connection issues:
1. Verify services are running: `docker-compose ps`
2. Check toolbox logs: `docker-compose logs toolbox`
3. Test the API: `curl http://localhost:5001/api/toolset/tickets_toolset`
