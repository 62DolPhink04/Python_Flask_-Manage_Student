# syntax=docker/dockerfile:1
FROM python:latest
WORKDIR /app

# Copy và cài đặt các dependencies
COPY requirement.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

# Thiết lập biến môi trường FLASK_APP cho tệp runserver.py
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=runserver.py

# Chạy Flask trên cổng 80 trong container
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
