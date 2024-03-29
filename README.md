# GOSPLAT
## Description
`(GoLang Static Package Language-model Analysis Tool)`; A tool to analyze packages and functions in GoLang and finding possible improvements to which package functions are placed in.

### Dynamic analysis which curates its choices to your code base
Gosplat uses the FastText model trained on a large number of open-source projects in GoLang in a curated manner so that it's able to find possible inconsistencies in your program structure. It checks if functions are in the right package, and can give possible packages to move functions to if they have a low match, also giving hints to packages with bad naming.

### Doesn't steal any data! :D
The FastText model is pre-trained and of course, will not by any means save any data of the projects it's used in. The model is downloaded from a GitLab repo and ready to be used afterwards.

## Goals of this project
Gosplat's and our goals are to create a nice, quick and easy way to analyze possible holes in your/your team's code structure. It may give helpful hints which can aid in creating a more maintainable environment for future projects to come!

## Install
### Dependencies
 - Golang
 - python3
 - pip (used to download python dependencies)
### How to
Simply run `install.sh` in the repo directory after cloning it and the rest is done for you

## Usage
Usage of gosplat has the structure:
```
gosplat -d [directory] -ns -a [0 - ...]
```
### Flags
- `-d` - Overrides the default directory given to gosplat which is current directory
- `-a` - Sets hitrate or "accuracy" of gosplat's analysis, the lower the higher hitrate on proposed mismatches
- `-ns` - Turning on naming suggestions if a proposed mismatch from model is accepted as an error

# Preprocessing/training
If you want to override the model that's currently available, or further build upon it in training, the preprocessor used for the data can be found in https://github.com/Gabriel-Ivarsson/gosplat-preprocessor.

The trainer can be found in https://github.com/Gabriel-Ivarsson/gosplat-trainer.

# Shout out to the Gensim library we used
 - If you want to check it out you can do so here: https://radimrehurek.com/gensim/
 
