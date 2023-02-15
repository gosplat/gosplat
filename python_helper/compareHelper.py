# Provides helper functions for doing comparisons using the provided model.
from colors import blue, green, red, yellow
from gensim.models import FastText


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
            green(model.wv.distance(package_name.lower(), function.lower())),
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
            package_name.lower(), function_name.lower())
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
        print(green(model.wv.most_similar(function.lower())))


def find_non_matching_function(function_list: list[str], model: FastText):
    """
    Takes function_list
    Finds function in list that matches the least with the other functions.

    Prints the name of that function.
    """
    print(blue("Results for word that least fits in given word list"))
    function_list = [function.lower() for function in function_list]
    print(red(model.wv.doesnt_match(function_list)))
