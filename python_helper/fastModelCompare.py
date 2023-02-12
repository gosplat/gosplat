#!/usr/local/bin/python
import argparse
import json
from typing import Any
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
        project_data:dict[str,Any] = json.loads(project_json)
        print(blue(project_data))
        # package_functions: Dictionary with key package name, containing all package functions.
        package_functions:dict[str,list[str]] = {}
        # get a packages functions and add them to dictionary.
        for package in project_data:
            # print(blue(package))
            # print(green(project_data[package]))
            package_files = project_data[package]["package_files"]
            # print(red(package_files))
            function_list:list[str] = []
            for file in package_files:
                functions:list[str] = file["functions"]
                if functions:
                    function_list.extend(functions)
            # print(yellow(function_list))
            # add function_list to current package in dictionary.
            package_functions[package.lower()] = function_list

            # print(red(project_data[package]["package_files"]))
        
        ## Present Results
        # compare function names to the package name they exists in.
        for package_name in package_functions:
            compare_package_function_list_distance(package_name, package_functions[package_name], model)
        # test
        compare_package_function_list_distance("routes", ["getuser", "execpythonmodel"], model)

        return

    # compare against model
    compare_package_function_list_distance(args.package_name, args.function_list, model)


if __name__ == "__main__":
    main()
