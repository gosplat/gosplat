#!/usr/local/bin/python
import argparse
import json
from compare_helper import GosplatSolver
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
        gosplatSolver = GosplatSolver()
        gosplatSolver.init(project_packages, model)
        for package in project_packages:
            functions = project_packages[package]["functions"]
            for function in functions or []:
                gosplatSolver.check_function(function, package)
        return


if __name__ == "__main__":
    main()
