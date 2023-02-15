#!/bin/bash
#
# Install script for gosplat
#
# Updating and moving dependencies to $HOME/.local/share/
git submodule update --init --recursive
mkdir -p $HOME/.local/share/gosplat
cp -r ./python_helper $HOME/.local/share/gosplat

# Building program binary
go install .
