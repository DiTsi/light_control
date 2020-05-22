FROM alpine:latest

RUN apk add --update \
    python3 \
    python3-dev \
    py3-virtualenv \
    build-base \
  && rm -rf /var/cache/apk/*

COPY ./app /app
COPY ./saved.txt /
RUN virtualenv -p /usr/bin/python3 /app/venv
RUN source /app/venv/bin/activate && pip install -r /app/requirements.txt

CMD /app/venv/bin/python3 /app/main.py