FROM ubuntu:16.04

MAINTAINER Brendan Harmon <brendan.harmon@gmail.com>

USER root

# system environment
ENV DEBIAN_FRONTEND noninteractive

# compile python
RUN apt-get update \
    && apt-get install -y \
      python-pip \
    && apt-get autoremove \
    && apt-get clean
RUN python -m pip install --upgrade pip
RUN python -m pip install numpy scipy matplotlib ipython jupyter pandas sympy nose ggplot

# compile latex
RUN apt-get install haskell-platform
RUN apt-get install texlive-full
RUN apt-get install texmaker
RUN apt-get install git-core

# compile r
apt-get install r-base

# copy jupyter notebook
RUN mkdir /data
WORKDIR /data
COPY hello-world.ipynb .

# create a user
RUN useradd -m -U jovyan

# change the owner so that the user can execute
RUN chown -R jovyan:jovyan /data

# switch the user
USER jovyan

CMD jupyter notebook --ip=0.0.0.0 --port=8080
