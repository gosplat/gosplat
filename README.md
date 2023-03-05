# gosplat (Go Static Package Language-model Analysis Tool)
## Description
A tool which can find lacking file structure. It checks if functions are in the right packages, can give possible packages to move functions into if they have a low match, and give hints to packages with bad naming.

### Dynamic analysis which curates its choices to your code base
Gosplat uses the FastText model trained on a large number of open-source projects in GoLang in a curated manner so that it's able to find ossible inconsistencies in your program structure. 

### Doesn't steal any data! :D
The FastText model is pre-trained and of course, will not by any means save any data of the projects it's used in. The model is downloaded from our gitlab repo and ready to be used afterwards.

## Goals of this project
Gosplat's and our goals are to create a nice, quick and easy way to analyze possible holes in your or your team's file structure. It may give helpful hints which can aid in creating a more maintainable enviorment for future projects to come!

## Install
### Dependencies
 - Golang 19.1
 - python3
### How to
Simply run `bash install.sh` in the repo folder after cloning it and the rest is done for you

# Big thanks to the people working on gensim
 - If you want to check them out you can do so here: https://radimrehurek.com/gensim/
