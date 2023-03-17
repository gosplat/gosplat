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

revert_changes () {
  rm "$HOME/.local/bin/gosplat" 2> /dev/null
  rm -rf "$HOME/.local/share/gosplat/" 2> /dev/null
}

echo; echo "*----- Installing Gosplat -----*"; echo

echo "Creating directories"
echo "$model_dest"
echo "$python_dest"; echo
mkdir -p "$HOME/.local/share/gosplat"
mkdir -p "$HOME/.local/share/gosplat/src" # create directories if they dont exists

# download model
echo "-----------------------------"; echo
echo "Downloading pre-trained model..."; echo
if curl -L -o "$tempfile" "$repo_link"; then # curl zip to tempfile
  unzip -q "$tempfile" "*.bin"
  echo "-- Success!"
else
  echo "Error; Failed to download model"
  revert_changes
  exit 1
fi

echo "-----------------------------"; echo
# install python dependencies
echo "Installing python dependencies"; echo
if python3 -m pip install -q -r "requirements.txt"; then
  echo "-- Success!"; echo
else
  echo "Error; Failed to download python dependencies"
  revert_changes
  exit 1
fi

# copy model to destination
echo "-----------------------------"; echo
echo "Copying model to $model_dest"; echo
if \cp "./$repo_dir/fast-fb-model.bin" "$model_dest"; then
  echo "-- Success!"
else
  echo "Error; Could not copy to $model_dest"
  revert_changes
  exit 1
fi

# copy python files to destination
echo "-----------------------------"; echo
echo "Copying python dependencies to $python_dest"; echo
if rsync --quiet -av --progress "./src/python_helper" "$python_dest" --exclude ./.git; then
  echo "-- Success!"
else
  echo "Error; Could not copy python dependencies to $python_dest"
  revert_changes
  exit 1
fi

# Building program binary
echo "-----------------------------"; echo
echo "Building binary..."; echo
if go build -o "gosplat" .; then
  echo "-- Success!"
else
  echo "Error; Failed to build binary"
  revert_changes
  exit 1
fi

echo "-----------------------------"; echo
echo "Copying built binary to $binary_dest"; echo
if \cp gosplat "$binary_dest"; then
  echo "-- Success!"
else
  echo "Error; Failed to copy binary to $binary_dest"
  revert_changes
  exit 1
fi

# clean up
rm -f $tempfile
rm -rf $repo_dir
rm -f "gosplat"

echo "- - - - - - - - - - - - - - -"; echo
# done
echo "Installation done!"
