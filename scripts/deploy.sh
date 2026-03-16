#!/bin/bash
set -euo pipefail

cd /srv/Personal-website

echo "Updating repository..."
git fetch origin
git reset --hard origin/main

echo "Building new image..."
podman build -t localhost/personal-website_web .

echo "Restarting service..."
systemctl restart container-personal-website

echo "Cleaning unused images..."
podman image prune -af

echo "Deployment complete."