#!/bin/bash
# Usage: ./docker-proxy-pull.sh image_name:tag

PROXY="http://127.0.0.1:7890"
IMAGE=$1

if [ -z "$IMAGE" ]; then
    echo "Usage: $0 <image_name:tag>"
    exit 1
fi

echo "Stopping system Docker..."
sudo systemctl stop docker docker.socket

echo "Starting temporary proxied daemon..."
# Launching with both HTTP and HTTPS proxies
sudo HTTP_PROXY=$PROXY HTTPS_PROXY=$PROXY dockerd > /dev/null 2>&1 &
DOCKERD_PID=$!

# Wait for daemon to be ready
echo "Waiting for daemon to initialize..."
sleep 5

echo "Pulling $IMAGE..."
docker pull $IMAGE

echo "Cleaning up..."
sudo kill $DOCKERD_PID
sleep 2

echo "Restarting system Docker..."
sudo systemctl start docker
echo "Done!"