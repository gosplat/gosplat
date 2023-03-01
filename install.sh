#!/bin/bash
#
# Install script for gosplat
#
# Updating and moving dependencies to $HOME/.local/share/
./src/modelGetter/modelGetter

mkdir -p $HOME/.local/share/gosplat
rsync -av --progress ./* $HOME/.local/share/gosplat --exclude ./.git
# Building program binary
go install .
