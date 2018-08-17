FROM jupyter/scipy-notebook:latest

MAINTAINER Brendan Harmon <brendan.harmon@gmail.com>

# system environment
ENV DEBIAN_FRONTEND noninteractive

USER root

# Create a Python 2.x environment using conda
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 ipython \
    ipykernel kernda numpy scipy matplotlib jupyter pandas sympy nose ggplot \
    && conda clean -tipsy

# Create a global kernelspec in the image and modify it
# to properly activate the python2 conda environment.
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install && \
$CONDA_DIR/envs/python2/bin/kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json

# copy jupyter notebook
RUN mkdir /data
WORKDIR /data
COPY myfirstnotebook.ipynb .

# create a user
RUN useradd -m -U jovyan

# change the owner so that the user can execute
RUN chown -R jovyan:jovyan /data

# switch the user
USER jovyan

CMD jupyter notebook --ip=0.0.0.0 --port=8080
