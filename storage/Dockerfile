FROM python:3.10-slim

WORKDIR /app
COPY storage.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn", "storage:app", "--host", "0.0.0.0", "--port", "8000"]
