# Provides helper functions for doing comparisons using the provided model.
from numbers import Number
from colors import blue, green, red, yellow
from gensim.models import FastText
import re


def sanitize_name(name: str) -> str:
    """
    Takes a string and sanitizes it to conform to camelCase naming convention
    and then make everything lowercase.

    Returns sanitized string.
    """
    return re.sub("[^a-zA-Z0-9 ]+", "", name).lower()

def calculateAverageDistance(distance_list: list[float]):
    size = len(distance_list)
    total = 0
    for x in distance_list:
        total += x
    return total/size

def mitigate_FPs(function_name: str, package_list: list[str], old_package_name: str, model: FastText, control_value: float):
    """
    Checks for if the function's match is less than the average deviation between function an all packages
    helps to mitigate false positives, will also decrease amount of true positives

    returns false if it is in a package with average deviation, true if it's in an outlier.
    """
    distance_list = []
    for package in package_list:
        distance = model.wv.distance(sanitize_name(package), sanitize_name(function_name))
        distance_list.append(distance)
    average_distance = calculateAverageDistance(distance_list)
    distance = model.wv.distance(sanitize_name(old_package_name), sanitize_name(function_name)) 
    if distance <= average_distance * control_value:
        return  True
    return False

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
        print(
            yellow(f"\tFunction '{function}':"),
            green(model.wv.distance(sanitize_name(
                package_name), sanitize_name(function))),
        )


def list_best_matching_package(function_name: str, package_list: list[str], old_package_name: str, model: FastText):
    """
    Takes a function_name, package_list, old_package_name and
    checks for the best matching package for the function in package_list

    Prints the results
    """
    best_match_package: str = find_best_matching_package(
        function_name, package_list, model)
    if best_match_package == old_package_name:
        print(
            green(f"Function: {function_name} already in best matching package '{old_package_name}'!"))
    else:
        if mitigate_FPs(function_name, package_list, old_package_name, model, 1) == False:
            print(
                red(f"Function: '{function_name}' in '{old_package_name}' package, is NOT in the best matching package, consider moving to '{best_match_package}' package!"))


def find_best_matching_package(function_name: str, package_list: list[str], model: FastText) -> str:
    """
    Takes a function_name and package_list and
    checks for the best matching package for the function,

    returns best matching package.
    """
    distances: dict[float, str] = {}
    for package_name in package_list:
        dist: float = model.wv.distance(
            sanitize_name(package_name), sanitize_name(function_name))
        distances[dist] = package_name

    dist_list: list[float] = list(distances.keys())
    smallest_distance: float = min(dist_list)
    best_match: str = distances[smallest_distance]
    return best_match


def list_most_similar(function_list: list[str], model: FastText):
    """
    Takes function_list and for each function
    checks for most similar words in training data,

    prints list of most similar word.
    """
    for function in function_list:
        print(blue(f'Results for words found similar to "{function}"'))
        print(green(model.wv.most_similar(sanitize_name(function))))


def find_non_matching_function(function_list: list[str], model: FastText):
    """
    Takes function_list
    Finds function in list that matches the least with the other functions.

    Prints the name of that function.
    """
    print(blue("Results for word that least fits in given word list"))
    function_list = [sanitize_name(function) for function in function_list]
    print(red(model.wv.doesnt_match(function_list)))
