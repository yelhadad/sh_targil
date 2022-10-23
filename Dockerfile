FROM ubuntu:latest
ENV VERSION='1.2.0'
RUN apt update
RUN apt install -y python3 vim zip unzip
RUN mkdir /tmp/text_files && mkdir /tmp/zipped_files && chmod 777 /tmp/*_files
COPY zip_job.py /tmp
CMD cat /etc/os-release; cat /tmp/zip_job.py
