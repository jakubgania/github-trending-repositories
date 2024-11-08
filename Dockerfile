FROM ubuntu:latest

RUN apt update && apt install -y python3.12 python3.12-venv python3-pip cron

WORKDIR /app

COPY . .

RUN python3.12 -m venv /app/venv

RUN /app/venv/bin/pip install --upgrade pip
RUN /app/venv/bin/pip install -r requirements.txt

RUN /app/venv/bin/playwright install --with-deps chromium firefox webkit

RUN echo "*/2 * * * * /app/venv/bin/python3.12 /app/scrape.py >> /var/log/cron.log 2>&1" > /etc/cron.d/scrape-cron
# COPY crontab /etc/cron.d/scrape-cron

RUN chmod 0644 /etc/cron.d/scrape-cron

# Apply cron job
RUN crontab /etc/cron.d/scrape-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

EXPOSE 8000

COPY start_services.sh /app/start_services.sh
RUN chmod +x /app/start_services.sh

CMD ["/app/start_services.sh"]

# CMD cron && /app/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
# CMD ["cron", "-f", "/app/venv/bin/python3.12", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["/app/venv/bin/python3.12", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]