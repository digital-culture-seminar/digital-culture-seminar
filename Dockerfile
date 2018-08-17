FROM jupyter/scipy-notebook:latest

MAINTAINER Brendan Harmon <brendan.harmon@gmail.com>

USER root

# system environment
ENV DEBIAN_FRONTEND noninteractive

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
