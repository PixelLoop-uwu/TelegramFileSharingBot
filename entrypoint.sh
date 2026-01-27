#!/bin/sh

# FastAPI. 
uv run uvicorn api.main4:app --host 0.0.0.0 --port 8000 &

# бота
uv run python -m bot.main4