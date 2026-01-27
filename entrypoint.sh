#!/bin/sh

# FastAPI. 
uv run uvicorn api.main4:api --host 0.0.0.0 --port 8000 &

# Tg
uv run python -m bot.main4