# dev-toolkit-39

A modular Python-based utility suite designed to accelerate daily development workflows through automated environment management and file processing. This toolkit simplifies repetitive CLI tasks, ensuring consistency across local development and CI/CD pipelines.

## Features

*   **Environment Validator:** Automatically checks for missing system dependencies, environment variables, and correct Python versions before project initialization.
*   **Log Purger:** An intelligent, regex-driven cleanup utility to safely archive or remove outdated log files and temp caches.
*   **Payload Transformer:** A robust interface to convert between JSON, YAML, and CSV formats with built-in schema validation.
*   **Dependency Auditor:** Quickly generates tree-based dependency reports to identify bloated or conflicting packages in your `requirements.txt`.

## Installation

Ensure you have Python 3.9+ installed. You can install the toolkit directly from the source:

```bash
git clone https://github.com/Developer/dev-toolkit-39.git
cd dev-toolkit-39
pip install -r requirements.txt
python setup.py install
```

## Basic Usage

The toolkit provides a unified entry point via the `dt39` CLI command. To validate your current environment and generate a dependency report, run:

```bash
dt39 check --audit
```

To convert a configuration file format:

```bash
dt39 transform --input config.json --output config.yaml
```

For a list of all available commands and flags, use the help flag:

```bash
dt39 --help
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the `LICENSE` file for details.