# 🤖 ADK Agents

## 🛠️ Setup

```sh
uv sync
source .venv/bin/activate
cp .env.example .env

gcloud auth login
gcloud config set project ${GOOGLE_CLOUD_PROJECT}
# enable vertexai and storage api

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
dk web --session_service_uri "sqlite:///./google_adk_agents.db" --memory_service_uri "agentengine://3732274628299587584"
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
- `"Update ticket #42 status to 'In Progress'"`
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
- `"Create a new corpus called 'product-docs'"`
- `"Upload the file 'manual.pdf' to the 'documents' bucket"`
- `"Import gs://my-bucket/docs/ into corpus 'product-docs'"`
- `"Search all corpora for 'how to reset the device'"`
- `"What files are in the 'knowledge-base' corpus?"`
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
