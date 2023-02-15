#!/bin/bash
#
# Install script for gosplat
#
# Updating and moving dependencies to $HOME/.local/share/
# TODO: curl model `.bin` file from somewhere...
mkdir -p $HOME/.local/share/gosplat
cp -r ./python_helper $HOME/.local/share/gosplat

# Building program binary
go install .
