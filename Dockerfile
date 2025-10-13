# set base image (host OS)
FROM linkml/linkml:1.9

USER root
ENV PATH=/root/.local/bin:$PATH

# Install jq so we can process JSON
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y --fix-missing \
    jq \
    nano \
    make \
    git

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  UV_VERSION=0.7.13

# Install uv
RUN pip install "uv==$UV_VERSION"
RUN uv tool install --with jinja2-time copier
RUN uv tool install rust-just

# set the working directory in the container
WORKDIR /work

#RUN pip install schema-automator
#RUN pip install appengine-python-standard
#RUN pip install cruft

# AIRR requirements
RUN pip install airr

RUN mkdir /ak-schema
COPY . /ak-schema

#RUN cd /ak-schema && make install
