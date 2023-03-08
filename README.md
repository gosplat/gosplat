# gosplat (GoLang Static Package Language-model Analysis Tool)
## Description
A tool to analyze packages and functions in GoLang and finding possible improvements to which package functions are placed in.

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

# Big thanks to the people working on gensim
 - If you want to check them out you can do so here: https://radimrehurek.com/gensim/
