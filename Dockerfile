# Use Python Alpine
FROM python:3.12-alpine3.20

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    libffi-dev \
    musl-dev \
    ffmpeg \
    aria2 \
    make \
    g++ \
    cmake \
    py3-setuptools

# Install Bento4 (your original logic kept)
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

# FIX pkg_resources issue permanently
RUN apk add --no-cache py3-setuptools && \
    python3 -m ensurepip && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r sainibots.txt && \
    python3 -m pip install yt-dlp

# Expose port (Render uses this)
ENV PORT=8000

# ✅ Run BOTH bot + web properly
CMD ["sh", "-c", "python3 modules/main.py & exec gunicorn app:app --bind 0.0.0.0:$PORT"]
