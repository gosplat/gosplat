#!/bin/bash
#
# Install script for gosplat
#
# Updating and moving dependencies to $HOME/.local/share/
mkdir -p $HOME/.local/share/gosplat/src
git clone https://gitlab.com/gaiv20/gosplat-models.git
mv ./gosplat-models/fast-fb-model.bin $HOME/.local/share/gosplat

mkdir -p $HOME/.local/share/gosplat
rsync -av --progress ./src/python_helper $HOME/.local/share/gosplat/src --exclude ./.git
# Building program binary
go build -o gosplat .
mv gosplat $HOME/.local/bin/
