# EOEPCA Testing Suite

## Disclaimer

This repository is a work in progress. It is not yet ready for use. \
The current proof of concept is available in the [final-proof-of-concept](https://github.com/jzvolensky/eoepca-testing/tree/final-proof-of-concept) branch of the project.

## Overview

This repository contains the EOEPCA Testing Suite, which is a set of tools to test the EOEPCA platform. It is primarly meant to test new deployments of the EOEPCA architecture.

The aim of this project is to provide a simple way to assess the status of the EOEPCA platform, and to provide a way to test the platform in a repeatable way.

## Requirements

- An EOEPCA kubernetes cluster deployment
  - See the [EOEPCA Deployment Guide](https://deployment-guide.docs.eoepca.org/current/) for examples on how to deploy the EOEPCA platform

## Installation

The EOEPCA Testing Suite is available as a python script.

1. Clone this repository

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Running the script

For now the script is run run from the main.py file which is located at the root of the repository.

```bash
scripts/main/main.py
```

The selection of tests is done by editing **scripts/config/default_config.yaml** where the tests to be run are specified.

## Tests

Currently the concept supports tests for the following components:

table 2x2

| Component | status |
| --------- | ------ |
| ADES      | Contains a single call to retrieve the processes available       |
| Resource Catalogue | Contains a single call to connect to the CSW endpoint       |
| Data Access Services     | Dummy function to show functionality       |
| Login Service | Dummy function to show functionality        |
| Workspace          | Dummy function to show functionality        |

## How to add a new component
The process has been made very simple to add a new component to the testing suite. The following steps are required:

1. Create a new folder within the **scripts** folder with the name of the component. This folder will contain the test files for the component.

2. Create a new python file within the folder created in step 1. This file will contain the test functions for the component. Optionally you can also create a logger for the component in **utils/utils.py**.

3. Register the component in the **scripts/component_actions/component_actions.py** which is used to call the test functions.

4. Add the relative path to your component to **/scripts/main/main.py (This is a temporary step, subject to change)

5. Add the component name to the configuration file **/scripts/config/default_config.yaml** to enable or disable the test for the component.
