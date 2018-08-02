FROM ubuntu:16.04

MAINTAINER Brendan Harmon <brendan.harmon@gmail.com>

# system environment
ENV DEBIAN_FRONTEND noninteractive

# compile jupyter
RUN apt-get update \
    && apt-get install -y \
      python-pip \
    && apt-get autoremove \
    && apt-get clean
RUN python -m pip install --upgrade pip
RUN python -m pip install jupyter

# copy jupyter notebook
RUN mkdir /data
WORKDIR /data
COPY myfirstnotebook.ipynb .

# create a user
RUN useradd -m -U jovian

# change the owner so that the user can execute
RUN chown -R jovian:jovian /data

# switch the user
USER jovian

CMD jupyter notebook --ip=0.0.0.0 --port=8080
