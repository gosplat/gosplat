# Provides helper functions for doing comparisons using the provided model.
from colors import blue, green, red
from gensim.models import FastText
import re


class GosplatSolver:
    averageDistance: float
    model: FastText
    package_list: list[str]
    function_list: list[str]

    def init(self, packages: dict[str, dict[str, list[str]]], model_p: FastText):
        self.model = model_p
        self.function_list = []
        self.package_list = []

        self.getPackageList(packages)
        self.getFunctionList(packages)
        self.calculateAverageDistance(packages)

    def getFunctionList(self, packages: dict[str, dict[str, list[str]]],):
        for package in packages:
            funcs = packages[package]["functions"]
            for function in funcs or []:
                self.function_list.append(function)

    def getPackageList(self, packages: dict[str, dict[str, list[str]]],):
        self.package_list = list(packages.keys())

    def calculateAverageDistance(self, packages: dict[str, dict[str, list[str]]],):
        total = 0
        comparisons = 0
        for package in packages:
            funcs = packages[package]["functions"]
            for function in funcs or []:
                total += self.model.wv.distance(package, function)
                comparisons += 1
        self.averageDistance = total/comparisons

    def sanitize_name(self, name: str) -> str:
        """
        Takes a string and sanitizes it to conform to camelCase naming convention
        and then make everything lowercase.

        Returns sanitized string.
        """
        return re.sub("[^a-zA-Z0-9 ]+", "", name).lower()

    def mitigate_FPs(self, function_name: str, package_name: str, control_value: int):
        """
        Checks for if the function's match is less than the average deviation between function an all packages
        helps to mitigate false positives, will also decrease amount of true positives. This can be steered with control value

        returns false if it is in a package with average deviation, true if it's in an outlier.
        """
        distance = self.model.wv.distance(function_name, package_name)
        if distance <= self.averageDistance * control_value:
            return True
        return False

    def find_best_matching_package(self, function_name: str):
        """
        Takes a function_name and package_list and
        checks for the best matching package for the function,

        returns best matching package.
        """
        distances: dict[float, str] = {}
        for package_name in self.package_list:
            dist: float = self.model.wv.distance(
                self.sanitize_name(package_name), self.sanitize_name(function_name))
            distances[dist] = package_name

        dist_list: list[float] = list(distances.keys())
        smallest_distance: float = min(dist_list)
        best_match: str = distances[smallest_distance]
        return best_match

    def check_function(self, function_name: str, old_package_name: str):
        """
        Takes a function_name, package_list, old_package_name and
        checks for the best matching package for the function in package_list

        Prints the results
        """
        best_match_package: str = self.find_best_matching_package(
            function_name)
        if best_match_package != old_package_name:
            if self.mitigate_FPs(function_name, old_package_name, 1) == False:
                print(
                    red(f"Function: '{function_name}' in '{old_package_name}' package, may NOT be in the best matching package, consider placing it in '{best_match_package}' or choosing a better name for {old_package_name}!"))

    def list_most_similar(self):
        """
        Takes function_list and for each function
        checks for most similar words in training data,

        prints list of most similar word.
        """
        for function in self.function_list:
            print(blue(f'Results for words found similar to "{function}"'))
            print(green(self.model.wv.most_similar(self.sanitize_name(function))))

    def find_non_matching_function(self):
        """
        Takes function_list
        Finds function in list that matches the least with the other functions.

        Prints the name of that function.
        """
        print(blue("Results for word that least fits in given word list"))
        function_list = [self.sanitize_name(
            function) for function in self.function_list]
        print(red(self.model.wv.doesnt_match(function_list)))
