#!/bin/bash
set -e

APP_NAME=Personal-website
SRC_DIR=/srv/Personal-website
BIN_PATH=/usr/local/bin/$APP_NAME

cd $SRC_DIR
git pull
cargo build --release

sudo cp target/release/Personal-website $BIN_PATH
sudo chmod 755 $BIN_PATH

sudo systemctl restart Personal-website

echo "Deploy complete."
