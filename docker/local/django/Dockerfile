# Dockerfile

# Python version
FROM python:3.10.0-slim-buster

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles

# Set work directory
WORKDIR $APP_HOME

LABEL maintainer='amiralibzdih@gmail.com'
LABEL description='development image for villaage project'

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

# we set pythonunbuffered to 1, that's means when we running our application we want python to print any output
#   directly to the console so it's dosen't buffer the output
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get -y install netcat gcc postgresql \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

# RUN pip3 install --upgrade click==8.0.2

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT [ "/entrypoint"]