# pywc

[![PyPI](https://img.shields.io/pypi/v/pywc.svg)](https://pypi.org/project/pywc/)
[![Changelog](https://img.shields.io/github/v/release/Akatama/pywc?include_prereleases&label=changelog)](https://github.com/Akatama/pywc/releases)
[![Tests](https://github.com/Akatama/pywc/actions/workflows/test.yml/badge.svg)](https://github.com/Akatama/pywc/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Akatama/pywc/blob/master/LICENSE)

Python version of wc command line tool

## Installation

Install this tool using `pip`:
```bash
pip install pywc
```
## Usage

For help, run:
```bash
pywc --help
```
You can also use:
```bash
python -m pywc --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd pywc
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
