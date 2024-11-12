# set base image (host OS)
FROM python:3.9

# Install jq so we can process JSON
RUN apt-get update
RUN apt-get install jq -y

# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_VERSION=1.1.13

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# set the working directory in the container
WORKDIR /work

RUN pip install schema-automator
RUN pip install appengine-python-standard
RUN pip install cruft

# AIRR requirements
RUN pip install airr

RUN mkdir /ak-schema
COPY . /ak-schema

RUN cd /ak-schema && make install
