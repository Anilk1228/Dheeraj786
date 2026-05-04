FROM python:3.12-alpine3.20

WORKDIR /app

COPY . .

# System deps
RUN apk add --no-cache \
    gcc \
    libffi-dev \
    musl-dev \
    ffmpeg \
    aria2 \
    make \
    g++ \
    cmake \
    bash \
    wget \
    unzip

# Bento4 install
RUN wget -q https://github.com/axiomatic-systems/Bento4/archive/v1.6.0-639.zip && \
    unzip v1.6.0-639.zip && \
    cd Bento4-1.6.0-639 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    cp mp4decrypt /usr/local/bin/ && \
    cd ../.. && \
    rm -rf Bento4-1.6.0-639 v1.6.0-639.zip

# 🔥 Python deps (FIX pkg_resources issue)
RUN python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools wheel && \
    pip3 install --no-cache-dir -r sainibots.txt && \
    pip3 install yt-dlp

# 🚀 Run bot + web
CMD ["bash", "-c", "python3 modules/main.py & gunicorn app:app --bind 0.0.0.0:$PORT"]
