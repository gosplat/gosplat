#!/bin/bash
#
# Install script for gosplat
#
# Updating and moving dependencies to $HOME/.local/share/
git submodule update --init --recursive
cp -r ../gopslat $HOME/.local/share

# Building program binary
go install .
