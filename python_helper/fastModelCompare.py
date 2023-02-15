#!/usr/local/bin/python
import argparse
import json

from colors import blue, green, red, yellow
from compareHelper import (
    compare_package_function_list_distance, find_non_matching_function, list_best_matching_package)
from gensim.models.fasttext import load_facebook_model


def main():
    # command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        dest="model_file", default="none", help="(Optional) Model file to load"
    )
    parser.add_argument(
        "-f",
        "--functions",
        dest="function_list",
        nargs="+",
        default=[str],
        help="List of function names to compare to package name",
        required=False,
    )
    parser.add_argument(
        "-p",
        "--package",
        dest="package_name",
        help="The Package Name to compare function list too",
        required=False,
    )
    parser.add_argument(
        "-j",
        "--json",
        dest="project_json",
        default="none",
        help="JSON of all functions and packages (To be used by go tool.)",
        required=False,
    )
    args = parser.parse_args()
    # assign project_json arg variable
    project_json: str = args.project_json

    # load model
    model = load_facebook_model(args.model_file)

    if args.project_json != "none":
        # parse data into dictionary
        project_packages: dict[str, dict[str, list[str]]
                               ] = json.loads(project_json)
        print(blue(project_packages))
        # Present Results
        # Compare function names vector distance to the package they exists in.
        for package_name in project_packages:
            compare_package_function_list_distance(
                package_name, project_packages[package_name]["functions"], model
            )
        # Find best matching package for each function
        # to see if any function should be moved.
        package_list: list[str] = list(project_packages.keys())
        for package_name in project_packages:
            # list best matching package
            funcs = project_packages[package_name]["functions"]
            for function_name in funcs or []:
                list_best_matching_package(
                    function_name, package_list, package_name, model)

        # test
        compare_package_function_list_distance(
            "pythonrunner", ["getuser", "ExecPythonModel"], model)

        return

    # compare against model
    compare_package_function_list_distance(
        args.package_name, args.function_list, model)


if __name__ == "__main__":
    main()
