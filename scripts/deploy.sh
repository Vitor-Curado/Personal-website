#!/bin/bash
set -e

cd /srv/personal-website

git pull

podman compose build
podman compose up -d