FROM fedora:latest

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN dnf update -y&& \
  dnf upgrade -y && \
  dnf install python3-pip curl -y && \
  pip3 install pipenv 

RUN pip3 install pandas
RUN pip3 install sklearn
RUN pip3 install -i https://test.pypi.org/simple/ --upgrade lambdata-nsriniva
COPY lambdata_test.py .
