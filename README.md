# ScamGuard AI
Objective: Build an LLM application for detecting scam messages.

LLM Used: flash-lite

## Steps to use repository
- Clone this repo
- Create a virtual environment
    - `Conda: conda create -n <venv_name> python==3.12 -y`
- Activate virtual environment
    - `Conda: conda activate <venv_name>`
- Install dependencies
    - `pip install -r requirements.txt`


## Project Folder
scam_guard_ai
- experiments
    - workflow.ipynb
    - workflow.py
- llm
    - prompts
        - react.md
    - prompts.py
- pipeline
    - scam_detector
        - builder.py
        - detector.py
        - executor.py
        - parser.py
- streamlit
    - app.py
- .gitignore
- LICENSE
- README.md
- main.py
- utils.py
- config.py
- requirements.txt

## Scam Detection AI Project Structure Description
- experiments >> Sandbox area for testing ideas and experiments
- workflow.ipynb - Notebook to experiment, test prompts, and run trial code
- llm - All Large Language Model–related code and assets
- prompts - Stores reusable LLM prompt templates and examples
- pipline - Core processing logic of the application
- scam_detector -Implements the scam detection workflow and decision logic
- streamlit -Frontend/UI layer for the application
- app.py - Streamlit app to take user input and display scam results
- main.py - Entry point to run scam detection without the UI
- utils.py - Common helper functions shared across modules
- config.py -Central place for configuration and environment settings
- requirements.txt - List of Python dependencies required to run the project