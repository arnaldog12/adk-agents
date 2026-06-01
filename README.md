# 🤖 ADK Agents

## 🛠️ Setup

```sh
uv sync
source .venv/bin/activate
cp .env.example .env

gcloud auth login
gcloud auth application-default login
gcloud config set project ${GOOGLE_CLOUD_PROJECT}
```

**Google Cloud Console — required setup:**

1. [Create an API Key][api-key] and add it to your `.env` file.
2. Create a GCS bucket and use this name when talking to Level 3 Agent.
3. Enable the following APIs:
   - Billing (and link a billing account)
   - Vertex AI API
   - Cloud Storage API
   - Agent Platform API
   - Cloud Resource Manager API
   - Vector Search API
4. In the [RAG Engine console][rag-engine], switch the RAG Engine to **serverless mode**.

**Memory service (Level 2):**

Run the script below once to provision the memory service on Agent Engine:

```sh
python memory_bank.py
```

## 🐳 1. Start the Database and Toolbox Services

```bash
docker-compose up -d

This starts:
- PostgreSQL database on port 5432
- Google Database Toolbox on port 5001 (port 5000 conflicts with macOS AirPlay)

### 🗒️ 2. Set Environment Variables

Change the environment variables in the `.env` file to your own.

## 🚀 3. Running

```bash
adk web --session_service_uri "sqlite:///./google_adk_agents.db" --memory_service_uri "agentengine://projects/294505191812/locations/us-central1/reasoningEngines/611885367682924544"


```
### 🧰 Level 1 (Agent + Tools + MCP - NL2SQL)

A bug ticket triage and debugging assistant for **QuantumRoast**, a coffee machine company. This agent demonstrates how to combine function tools, built-in tools (Google Search), and MCP Toolbox for SQL-based ticket management.

**Capabilities:**
- Create, search, and update bug tickets in a PostgreSQL database
- Search for similar/duplicate tickets using vector search
- Query tickets by date range, assignee, status, or priority
- Web search for known issues (CVEs, widespread problems)

**Example messages:**
- `"Show me all open P0 tickets"`
- `"Create a new ticket: the espresso machine is overheating after 5 minutes of use"`
- `"Find tickets similar to 'grinder motor failure'"`
- `"What tickets were created in the last week?"`
- `"Update ticket #1 status to 'In Progress'"`
- `"Search the web for known issues with coffee machine temperature sensors"`

---

### 🧠 Level 2 (Session + Memory + callbacks)

A conversational assistant with **persistent memory** across sessions. This agent demonstrates session management, memory services, and after-agent callbacks for automatic session saving.

**Capabilities:**
- Remember context from previous conversations
- Automatically save sessions to memory after each interaction
- Preload relevant memories at the start of new sessions

**Example messages:**
- `"Remember that my favorite programming language is Python"`
- `"What did we discuss last time?"`
- `"I mentioned a project earlier, can you remind me what it was?"`
- `"My name is Alex and I work on machine learning projects"`
- `"What do you know about me?"`

---

### 📚 Level 3 (Knowledge + RAG + Reasoning)

A **RAG (Retrieval Augmented Generation)** management agent for Vertex AI and Google Cloud Storage. Uses built-in planning with thinking capabilities for complex reasoning tasks.

**Capabilities:**
- Create, list, update, and delete RAG corpora in Vertex AI
- Upload files to GCS buckets and import them into corpora
- Search across all corpora or query specific ones
- Manage GCS buckets and files

**Example messages:**
- `"List all my RAG corpora"`
- `"List all my buckets"`
- `"Create a new corpus called 'product-docs'"`
- `"faz upload desse documento para um bucket chamado "arnaldo-bucket"`
- `"faça upload desse documento no corpora"`
- `"quais arquivos tem no meu corpora?"`
- `"qual a data da minha viagem?"`
- `"qual o preço total?"`
- `"qual o endereço do hotel?"`
- `"Delete corpus 'old-data'"`

---

### 🤖🤖 Level 4 (Multi-Agents)

A **multi-agent system** simulating a software development team with a Product Manager, Developer, and QA Engineer. Demonstrates agent orchestration and delegation patterns.

**Agents:**
- **Product Manager**: Defines features and orchestrates the workflow
- **Developer**: Implements Python code based on requirements
- **QA Engineer**: Tests the generated code and reports issues

**Capabilities:**
- Define product features collaboratively
- Generate Python code implementations
- Run and test code in a sandboxed environment
- Iterate based on test results

**Example messages:**
- `"Build a calculator that can add, subtract, multiply, and divide"`
- `"Create a function to check if a number is prime"`
- `"I need a class to manage a todo list with add, remove, and list methods"`
- `"Write a function to convert temperatures between Celsius and Fahrenheit"`
- `"Build a simple password generator"`

[api-key]: https://aistudio.google.com/app/api-keys
[rag-engine]: https://console.cloud.google.com/agent-platform/rag/corpus