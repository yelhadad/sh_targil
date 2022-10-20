FROM ubuntu:latest
ENV VERSION = 1.2.0
RUN apt update
RUN apt install -y python3 vim zip unzip
RUN mkdir text_files && mkdir ziped_files
COPY zip_job.py /tmp
CMD cat /etc/os-release; cat /tmp/zip_job.py
