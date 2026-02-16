#!/bin/bash
set -e

APP_NAME=Personal-website
SRC_DIR=/srv/Personal-website
BIN_PATH=/usr/local/bin/$APP_NAME

echo "Deploying $APP_NAME..."
cd $SRC_DIR

echo "Pulling latest changes from git..."
git pull

echo "Building the application..."
cargo build --release

echo "Stopping service..."
sudo systemctl stop $APP_NAME

echo "Copying binary to $BIN_PATH..."
sudo cp target/release/$APP_NAME $BIN_PATH
sudo chmod 755 $BIN_PATH

echo "Restarting service..."
sudo systemctl restart $APP_NAME

echo "Deploy complete."
