[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# dev-toolkit-39

dev-toolkit-39 is a Python toolkit offering command-line utilities to assist with common developer tasks such as project inspection and setup. It focuses on reducing the overhead of repetitive workflows in software development.

## Features

- Performs static analysis to identify code smells and potential bugs across Python files
- Manages isolated environments and installs dependencies based on project requirements
- Generates new projects from templates including tests, documentation, and CI configurations
- Provides utilities to search and summarize large log files from application runs

## Installation

Install the package using pip:

```bash
pip install dev-toolkit-39
```

For development installation from the repository:

```bash
git clone https://github.com/Developer/dev-toolkit-39.git
cd dev-toolkit-39
pip install -e .
```

## Usage

The primary interface is the `dtk` command-line tool.

```bash
dtk analyze my_project/
```

Integrate directly in Python scripts:

```python
from dev_toolkit_39.analysis import CodeAnalyzer

analyzer = CodeAnalyzer()
report = analyzer.scan("my_project")
print(report.issues)
```