# set base image (host OS)
FROM python:3.9

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
RUN pip install cruft

RUN mkdir /ak-schema
COPY . /ak-schema

RUN cd /ak-schema && make install

# Install these two packages required for schema-automator.
# Notes: This downgrades the urllib3 version to urllib3-1.26.18
# poetry.lock states that it requires urllib3 = ">=1.21.1,<3"
# so this should be fine.
RUN pip install appengine-python-standard
RUN pip install quantulum3[classifier]
