FROM nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04

WORKDIR /root
RUN apt-get update -y && apt-get install -y python3-pip \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install faster-whisper

COPY infer.py ./

WORKDIR /app
ENTRYPOINT ["python3", "/root/infer.py"]
