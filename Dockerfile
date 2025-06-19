FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt && \
  pip install "fastapi[all]"

COPY . .

CMD ["uvicorn", "main:app","--workers","8", "--host", "0.0.0.0", "--port", "8000"]
