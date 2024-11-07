#!/bin/bash

# Start cron in the background
# cron

# Start cron
service cron start

# Start uvicorn in the foreground so Docker keeps the container running
/app/venv/bin/python3.12 -m uvicorn main:app --host 0.0.0.0 --port 8000

# Keep the container running and log cron output
tail -f /var/log/cron.log