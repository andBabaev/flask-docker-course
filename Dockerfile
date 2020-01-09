FROM python:3.6-slim


ADD ./webapp /root/webapp
WORKDIR /root/webapp

RUN pip install --no-cache-dir -r /root/webapp/requirements.txt

ENV FLASK_APP=hello.py
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=True

CMD gunicorn -b 0.0.0.0:$PORT hello:app --reload
#CMD gunicorn -b 0.0.0.0:5000 hello:app --reload 