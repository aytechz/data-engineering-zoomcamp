FROM python:3.9.18

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2
# sqlalchemy psycopg2

WORKDIR /app
# COPY pipeline.py pipeline.py
COPY ingest_data.py ingest_data.py


ENTRYPOINT [ "python", "ingest_data.py"]