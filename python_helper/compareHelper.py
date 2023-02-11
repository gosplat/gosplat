# Provides helper functions for doing comparisons using the provided model.
from gensim.models import FastText
from colors import green, red, blue

def compare_package_function_list_distance(package_name: str, function_list: list[str], model: FastText):
    """
    Checks a list of functions against a package name
    and compares the distance between each function and the package name.
    """
    if not function_list:
        # if list is empty
        print(red(f"Error: No functions in package {package_name}."))
        return

    for function in function_list:
        print(blue(f"Results for words found similar to \"{function}\""))
        print(green(model.wv.most_similar(function)))

    for function in function_list:
        print(blue(f"Results for package name '{package_name}', compared to '{function}'"))
        print(green(model.wv.distance(package_name, function)))
    
    print(blue("Results for word that least fits in given word list"))
    print(red(model.wv.doesnt_match(function_list)))

