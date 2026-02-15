# Prefect Workflow Module

This module contains Prefect flows for the JobRunner project.

## Local Development Setup

To run Prefect flows against a local Dockerized server instead of Prefect Cloud, follow these steps:

### 1. Start Prefect Server

Ensure the Docker containers are running:

```bash
docker-compose up -d
```

This starts the Prefect Server at `http://localhost:4200`.

### 2. Configure Local Profile

Create a `local` profile to point to the local server and avoid conflicts with Prefect Cloud credentials.

```bash
# Create a new profile named 'local'
prefect profile create local

# Set the API URL to the local Docker instance
prefect config set -p local PREFECT_API_URL=http://127.0.0.1:4200/api

# Activate the local profile
prefect profile use local
```

To verify the configuration:

```bash
prefect config view
```

It should show `PREFECT_API_URL='http://127.0.0.1:4200/api'`.

### 3. Run a Test Flow

You can run a flow directly from your terminal.

```bash
uv run modules/workflow/test.py
```

Or with standard python:

```bash
python modules/workflow/test.py
```

## How It Works (Execution Model)

When you run `python test.py` locally:

1.  **Client Execution**: The Python process running in your terminal acts as the **Flow Runner**. It executes the code right there on your machine (not inside the Docker container).
2.  **API Communication**: The script communicates with the Prefect API Server (running in Docker at `localhost:4200`) to:
    - Register the Flow Run.
    - Report task states (Running, Completed, Failed).
    - Send logs.
3.  **No "Worker" Needed**: For direct script execution, you don't need a separate Prefect Worker or Work Pool. Your local process _is_ the worker for that specific run (often called an "ephemeral" worker).

To use actual **Workers** (e.g., for scheduled deployments):

1.  Define a Deployment (`prefect.yaml` or `.deploy()`).
2.  Start a worker process pointing to a Work Pool (`prefect worker start --pool default-agent-pool`).
3.  The API Server will queue runs, and the Worker will pick them up and execute them.
