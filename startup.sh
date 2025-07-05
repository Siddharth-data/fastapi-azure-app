#!/bin/bash

# Install required packages
pip install -r requirements.txt

# Start the FastAPI app from app/main.py with module path app.main:app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000