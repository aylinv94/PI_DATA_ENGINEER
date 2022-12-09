FROM python:3.10.6

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload
