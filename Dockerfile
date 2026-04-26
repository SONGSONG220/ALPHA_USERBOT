FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install -y \
    git curl ffmpeg \
    pkg-config \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt

CMD ["bash", "start.sh"]
