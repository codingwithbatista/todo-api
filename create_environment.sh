#!/bin/bash

python -m venv .todo-api-venv;
chmod +x .todo-api-venv/bin/activate;
source .todo-api-venv/bin/activate;
pip install -r requirements.txt
