#!/bin/bash
#
# Install script for gosplat
#
# Updating and moving dependencies to $HOME/.local/share/

tempfile="tempfile.zip"
repo_link="https://gitlab.com/gaiv20/gosplat-models/-/archive/main/gosplat-models-main.zip"
repo_dir="gosplat-models-main"
model_dest="$HOME/.local/share/gosplat"
python_dest="$HOME/.local/share/gosplat/src"
binary_dest="$HOME/.local/bin/"

echo; echo "--- Installing Gosplat ---"; echo

echo "Creating directories"
echo "$model_dest"
echo "$python_dest"; echo
mkdir -p "$HOME/.local/share/gosplat"
mkdir -p "$HOME/.local/share/gosplat/src" # create directories if they dont exists

# download model
echo "Downloading pre-trained model..."; echo
curl -L -o "$tempfile" "$repo_link" # curl zip to tempfile
unzip "$tempfile" "*.bin"
echo

# copy model to destination
echo "-----------------------------"; echo
echo "Copying model to $model_dest"; echo
\cp "./$repo_dir/fast-fb-model.bin" "$model_dest"

# copy python files to destination
echo "Copying python dependencies to $python_dest"; echo
rsync --quiet -av --progress "./src/python_helper" "$python_dest" --exclude ./.git

# Building program binary
echo "Building binary..."; echo
go build -o "gosplat" .
echo "Copying built binary to $binary_dest"; echo
\cp gosplat "$binary_dest"

# clean up
rm -f $tempfile
rm -rf $repo_dir
rm -f "gosplat"

# done
echo "Installation done!"
