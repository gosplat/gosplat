# Provides helper functions for doing comparisons using the provided model.
from gensim.models import FastText
from colors import green, red, blue, yellow

def compare_package_function_list_distance(package_name: str, function_list: list[str], model: FastText):
    """
    Checks a list of functions against a package name
    and compares the distance between each function and the package name.

    Prints the results.
    """
    if not function_list:
        # if list is empty
        print(red(f"Error: No functions in package {package_name}."))
        return

    print(blue(f"Results for package '{package_name}':"))
    for function in function_list:
        print(yellow(f"\tFunction '{function}':"), green(model.wv.distance(package_name, function)))


def list_best_matching_package(function_list: list[str], model: FastText):
    """
    Takes a function_name and package_list and
    checks for the best matching package for the function,

    returns best matching package.
    """


def list_most_similar(function_list: list[str], model: FastText):
    """
    Takes function_list and for each function
    checks for most similar words in training data,

    prints list of most similar word.
    """
    for function in function_list:
        print(blue(f"Results for words found similar to \"{function}\""))
        print(green(model.wv.most_similar(function)))


def find_non_matching_function(function_list: list[str], model: FastText):
    """
    Takes function_list
    Finds function in list that matches the least with the other functions.

    Prints the name of that function.
    """
    print(blue("Results for word that least fits in given word list"))
    print(red(model.wv.doesnt_match(function_list)))

