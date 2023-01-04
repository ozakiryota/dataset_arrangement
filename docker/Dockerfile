########## Pull ##########
FROM nvidia/cuda:11.6.2-base-ubuntu20.04
########## Non-interactive ##########
ENV DEBIAN_FRONTEND=noninteractive
########## Common Tools ##########
RUN apt-get update && \
    apt-get install -y \
	    vim \
    	wget \
    	unzip \
    	git \
		python3-tk
########## Dependencies ##########
RUN apt-get update && \
    apt-get install -y \
	    python3-pip \
		libgl1-mesa-dev \
		libgtk2.0-dev \
		imagemagick && \
	pip3 install \
		opencv-python \
		pillow
########## Cache Busting ##########
ARG CACHEBUST=1
########## dataset_arrangement ##########
RUN cd ~ && \
	git clone https://github.com/ozakiryota/dataset_arrangement.git
########## Initial Position ##########
WORKDIR /root/dataset_arrangement