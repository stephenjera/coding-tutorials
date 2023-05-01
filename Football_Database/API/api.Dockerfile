FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD ["python", "./app.py"]
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]