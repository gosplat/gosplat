#!/usr/local/bin/python
import sys
from colors import green, red, blue
from gensim.models.fasttext import load_facebook_model
from gensim.models import FastText

def main():
    one = sys.argv[1]
    two = sys.argv[2]
    three = sys.argv[3]
    print(green(one))
    print(blue(two))
    print(red(three))
if __name__ == "__main__":
    main()
