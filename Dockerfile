FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY  . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

