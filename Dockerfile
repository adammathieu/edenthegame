# VERSION 0.1.0
FROM python:latest
MAINTAINER Mathieu Adam <adammathieu@gmail.com>

# Install dependencies
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

# Add server code
ADD app.py /tmp/app.py
ADD gunicorn_settings.py /tmp/gunicorn_settings.py
WORKDIR /tmp

# Set Env variable
EXPOSE 5000
ENV FLASK_ENV="docker"

# Run the app
ENTRYPOINT ["/usr/local/bin/gunicorn","-c","/tmp/gunicorn_settings.py","app:app"]
