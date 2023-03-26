FROM python:3.10.10-bullseye
COPY . ./
RUN pip3 install -r ./requirements.txt
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 flaskcrud:app
