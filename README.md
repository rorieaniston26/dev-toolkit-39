# dev-toolkit-39

A modular Python-based utility suite designed to streamline local development workflows and automate routine system tasks. This toolkit minimizes boilerplate overhead by providing a unified interface for file management, environment synchronization, and task orchestration.

## Features

*   **Config Sync:** Automatically synchronize project configuration files and environment variables across multiple local environments.
*   **Log Auditor:** A lightweight parser to identify, aggregate, and report errors across complex directory trees.
*   **Process Supervisor:** A simple abstraction layer to manage and monitor long-running background tasks or local microservices.
*   **Path Manager:** Smart path mapping for dynamic cross-platform script execution without hardcoded strings.

## Installation

Ensure you have Python 3.9+ installed. You can install the toolkit directly via pip:

```bash
# Clone the repository
git clone https://github.com/Developer/dev-toolkit-39.git
cd dev-toolkit-39

# Install dependencies
pip install -r requirements.txt

# Run the installer
python setup.py install
```

## Basic Usage

Once installed, you can trigger individual modules via the command-line interface. For instance, to audit logs in a specific project directory, use:

```bash
dev-toolkit-39 audit --path ./my-project/logs --severity WARNING
```

To sync your current environment settings to your `~/.config` profile, simply run:

```bash
dev-toolkit-39 sync --profile default
```

For a full list of available flags and module parameters, use the help command:

```bash
dev-toolkit-39 --help
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.