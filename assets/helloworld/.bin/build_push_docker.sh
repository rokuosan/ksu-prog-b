#! /bin/sh

docker buildx build \
    -t ghcr.io/tamada/helloworld:latest \
    -t ghcr.io/tamada/helloworld:1.0.0 \
    --platform linux/amd64,linux/arm64 \
    --push .