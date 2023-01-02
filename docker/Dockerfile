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
########## Cache Busting ##########
ARG CACHEBUST=1
########## dataset_arrangement ##########
RUN cd ~ && \
	git clone https://github.com/NVIDIA/dataset_arrangement.git
########## Initial Position ##########
WORKDIR /root/dataset_arrangement