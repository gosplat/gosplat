#!/usr/local/bin/python
import argparse
import json
from gensim.models.fasttext import load_facebook_model
from gensim.models import FastText
from colors import green, red, blue

def compare_function_list(package_name: str, function_list: list[str], model: FastText):
    """
    Checks a list of functions against a package name
    and compares the distance between each function and the package name.
    """
    if not function_list:
        # if list is empty
        print(red("Error: No functions were provided as input"))
        return

    for function in function_list:
        print(blue(f"Results for words found similar to \"{function}\""))
        print(green(model.wv.most_similar(function)))

    for function in function_list:
        print(blue(f"Results for package name '{package_name}', compared to '{function}'"))
        print(green(model.wv.distance(package_name, function)))
    
    print(blue("Results for word that least fits in given word list"))
    print(red(model.wv.doesnt_match(function_list)))


def main():
    # command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(dest = "model_file", default="none", help="(Optional) Model file to load")
    parser.add_argument("-f", "--functions", dest = "function_list", nargs='+', default=[str], help="List of function names to compare to package name", required=False)
    parser.add_argument("-p", "--package", dest = "package_name", help="The Package Name to compare function list too", required=False)
    parser.add_argument("-j", "--json", dest = "project_json", default="none", help="JSON of all functions and packages (To be used by go tool.)", required=False)
    args = parser.parse_args()
    # assign project_json arg variable
    print(args.project_json)
    project_json: str = args.project_json

    # load model
    model = load_facebook_model(args.model_file)
    
    if args.project_json != "none":
        # TODO: parse object and compare each packages functions against the package name
        project_data = json.loads(project_json)
        print(green(project_data))
        print(red(project_data))
        print(blue(project_data))
        return

    # compare against model
    compare_function_list(args.package_name, args.function_list, model)


if __name__ == "__main__":
    main()
