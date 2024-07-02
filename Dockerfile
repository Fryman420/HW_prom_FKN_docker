FROM python:3.8-slim

WORKDIR /app

COPY ./backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend /app

RUN python init_db.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
