FROM python:3.11.11-slim

WORKDIR /usr/src/app

RUN pip install "fastapi[standard]"

COPY main.py .

CMD ["fastapi", "run", "main.py"]