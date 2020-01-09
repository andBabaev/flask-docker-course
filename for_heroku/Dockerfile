FROM python:3.6-slim


ADD ./webapp /root/webapp
ADD ./requirements.txt /temp/requirements.txt
WORKDIR /root/webapp

RUN pip install --no-cache-dir -r /temp/requirements.txt

ENV FLASK_APP=hello.py
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=True

CMD gunicorn -b 0.0.0.0:$PORT hello:app --reload