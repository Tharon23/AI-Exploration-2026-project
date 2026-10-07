---
name: setup
description: How to set up the development environment, configure tools, and verify installation.
triggers:
  - "setup"
  - "install"
  - "getting started"
  - "env"
edges:
  - target: context/stack.md
    condition: when checking which tools need to be installed
  - target: context/team.md
    condition: when setting up contributor-specific configuration
last_updated: 2026-10-07
---

# Development Environment Setup

## Prerequisites

- Python 3.11+
- Git 2.40+
- Node.js 18+ (for `npx promexeus` CLI)
- Docker & Docker Compose (for deployment verification)

## Quick Start (3 Contributors)

1. **Clone repository**:
   ```bash
   git clone <repo-url>
   cd AI-Exploration-2026-project
   ```

2. **Install pre-commit hooks**:
   - On Linux / macOS:
     ```bash
     bash scripts/setup-hooks.sh
     ```
   - On Windows (PowerShell):
     ```powershell
     powershell -ExecutionPolicy Bypass -File scripts\setup-hooks.ps1
     ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env and set your CONTRIBUTOR_NAME (kalab, bartek, or kamil) + API keys
   ```

4. **Verify setup**:
   ```bash
   npx promexeus check
   ```
