# syntax=docker/dockerfile:1
#My image inherites from "python" image
FROM python:latest
WORKDIR /app
#host: your PC, laptop, cloud server,...
#Copy from "host" to "container"
COPY requirements.txt /app/
#Run this command in the container
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY . /app/

# Thiết lập biến môi trường FLASK_APP cho tệp runserver.py
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=runserver.py

#Run command in container
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=5555"]
