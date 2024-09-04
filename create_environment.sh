#!/bin/bash

python -m venv .todo-api-venv;
chmod +x .todo-api-venv/bin/activate;
source .todo-api-venv/bin/activate;
pip install -r requirements.txt
#pip install "uvicorn[standard]";
#pip install fastapi;
#pip install "fastapi[standard]";
#pip install psycopg2-binary;
