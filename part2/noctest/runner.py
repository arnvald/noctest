import importlib.machinery
import types
from inspect import getmembers, isfunction
import sys
import os
from . import colors
from .expectation import FailedExpectationError

class Runner:
    def __init__(self, path):
        self.test_files = []
        self.successes, self.failures = 0, 0
        self.load_test_files(path)

    def load_test_files(self, path):
        if path.endswith("__pycache__"):
            return
        if os.path.isfile(path):
            self.test_files.append(path)
        elif os.path.isdir(path):
            for nested_path in os.listdir(path):
                self.load_test_files(path + "/" + nested_path)

    def load_tests(self, mod):
        return [m for m in getmembers(mod) if isfunction(m[1]) and m[0].startswith("test_")]

    def load_module(self, file):
        loader = importlib.machinery.SourceFileLoader("testmod", file)
        mod = types.ModuleType("testmod")
        loader.exec_module(mod)
        return mod

    def run_single_file(self, file):
        mod = self.load_module(file)
        tests = self.load_tests(mod)
        for test in tests:
            (test_name, test_function) = test
            try:
                test_function()
                self.successes += 1
                print(f"{test_name} - success")
            except FailedExpectationError as e:
                print(f"{colors.RED}{test_name} - failure: {e.message}{colors.RESET}")
                self.failures += 1
            except AssertionError:
                print(f"{colors.RED}{test_name} - failure{colors.RESET}")
                self.failures += 1

    def run(self):
        for test_file in self.test_files:
            self.run_single_file(test_file)

        print("\n============")
        print(f"Total number of tests: {self.successes + self.failures}")
        if self.failures == 0:
            print(f"{colors.GREEN}tests succeeded{colors.RESET}")
        else:
            print(f"{colors.RED}{self.failures} tests failed{colors.RESET}")

def main():
    Runner(sys.argv[1]).run()
