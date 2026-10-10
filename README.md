# dev-toolkit-39

A robust Python-based CLI utility designed to streamline daily development workflows by automating repetitive environment and project management tasks. It serves as a Swiss-army knife for developers seeking to reduce boilerplate and improve terminal-based productivity.

## Features

*   **Project Scaffolding:** Generate standardized folder structures and configuration files instantly using customizable templates.
*   **Environment Sync:** Effortlessly synchronize local development environment variables and dependency manifests across multiple machines.
*   **Log Analytics:** Quickly parse and sanitize local application logs using built-in regex-based filtering tools.
*   **Alias Management:** Centralized command-line registry to organize and execute frequently used shell scripts with short, memorable triggers.

## Installation

Ensure you have Python 3.9+ installed. You can install the toolkit via pip:

```bash
pip install dev-toolkit-39
```

To enable shell autocompletion, run:

```bash
dtk --install-completion
```

## Usage

Initialize a new project structure in your current directory:

```bash
dtk init my-new-project --template web-app
```

Parse and filter a specific log file for error codes:

```bash
dtk logs analyze app.log --filter "ERROR" --output report.txt
```

Run a custom script registered in your alias registry:

```bash
dtk run <alias_name>
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.