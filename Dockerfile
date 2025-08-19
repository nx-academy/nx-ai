FROM python:3.13-slim-bullseye AS base

# Dev env - For local development with DevContainer
FROM base AS dev
WORKDIR /workspaces/nx-ai
RUN pip install pytest

# Test env - For CI with GitHub Actions
FROM dev AS test
WORKDIR /test-app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "pytest" ]
