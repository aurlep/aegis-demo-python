FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
# Threaded, not the single synchronous worker gunicorn defaults to: an
# authenticated DAST scan opens many connections at once and a one-request-
# at-a-time server stalls it until the scanner gives up.
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "2", "-k", "gthread", "--threads", "8", "--timeout", "60", "app:app"]
