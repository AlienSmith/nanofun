FROM python:3.11-slim

# Install system dependencies (FFmpeg is key for your audio workers)
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install the latest stable Nanobot (v0.1.4.post6)
# This bypasses GHCR and uses standard HTTPS which your proxy likes
RUN pip install --no-cache-dir \
    nanobot-ai==0.1.4.post6 \
    mcp \
    httpx

WORKDIR /workspace