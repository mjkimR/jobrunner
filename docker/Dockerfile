FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy project files
COPY pyproject.toml uv.lock ./
COPY src ./src

# Sync dependencies
RUN uv sync --frozen --no-dev

# Set environment
ENV PYTHONPATH=/app/src
ENV DAGSTER_HOME=/app

CMD ["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]
