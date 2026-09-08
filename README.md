# dev-toolkit-39

A robust Python-based CLI suite designed to streamline common developer workflows and system automation tasks. This toolkit minimizes repetitive boilerplate by providing high-performance utilities for environment management, data processing, and file system orchestration.

## Features

*   **Task Automator:** Execute complex shell pipelines and multi-step deployment scripts with a unified interface.
*   **EnvSync:** Effortlessly synchronize and validate environment variables across development, staging, and production configurations.
*   **Log Purger:** A high-speed utility for rotating, compressing, and archiving system logs to reclaim disk space.
*   **JSON-to-CSV Converter:** Rapidly transform deeply nested configuration files into structured formats for external reporting.

## Installation

Ensure you have Python 3.8+ installed. You can install the toolkit via pip:

```bash
pip install dev-toolkit-39
```

To install from source for local development:

```bash
git clone https://github.com/Developer/dev-toolkit-39.git
cd dev-toolkit-39
pip install -e .
```

## Usage

Once installed, you can access the toolkit directly from your terminal.

**Syncing environment variables:**
```bash
dev-toolkit env-sync --source .env.example --target .env
```

**Compressing logs in a specific directory:**
```bash
dev-toolkit purge --path /var/log/myapp --retention 30
```

For a full list of commands and configuration options, run:
```bash
dev-toolkit --help
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.