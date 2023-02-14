#!/usr/local/bin/python
import argparse
import json
from colors import green, red, blue, yellow
from gensim.models.fasttext import load_facebook_model
from compareHelper import compare_package_function_list_distance

def main():
    # command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(dest = "model_file", default="none", help="(Optional) Model file to load")
    parser.add_argument("-f", "--functions", dest = "function_list", nargs='+', default=[str], help="List of function names to compare to package name", required=False)
    parser.add_argument("-p", "--package", dest = "package_name", help="The Package Name to compare function list too", required=False)
    parser.add_argument("-j", "--json", dest = "project_json", default="none", help="JSON of all functions and packages (To be used by go tool.)", required=False)
    args = parser.parse_args()
    # assign project_json arg variable
    project_json: str = args.project_json

    # load model
    model = load_facebook_model(args.model_file)
    
    if args.project_json != "none":
        ## parse data into dictionary
        project_packages:dict[str,dict[str,list[str]]] = json.loads(project_json)
        print(blue(project_packages))
        ## Present Results
        # Compare function names vector distance to the package they exists in.
        for package_name in project_packages:
            compare_package_function_list_distance(package_name, project_packages[package_name]["functions"], model)
        # Find best matching package for each function to see if any function should be moved.
        for package_name in project_packages:
            # todo best matching package
        # test
        compare_package_function_list_distance("routes", ["getuser", "execpythonmodel"], model)

        return

    # compare against model
    compare_package_function_list_distance(args.package_name, args.function_list, model)


if __name__ == "__main__":
    main()
