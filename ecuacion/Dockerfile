FROM python:3.10-slim

WORKDIR /microservicios
COPY ecuacionMulty.py .

RUN pip install fastapi uvicorn pydantic requests

CMD ["uvicorn", "ecuacionMulty:app", "--host", "0.0.0.0", "--port", "8000"]
