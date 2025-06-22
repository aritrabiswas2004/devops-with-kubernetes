FROM python:3.11

WORKDIR /app

COPY log-reader.py .
COPY outputs.log .

RUN pip install flask

EXPOSE 3000

CMD ["python3", "log-reader.py"]

