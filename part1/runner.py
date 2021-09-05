import importlib.machinery
import types
from inspect import getmembers, isfunction
import sys
import os
import colors

class Runner:
    def __init__(self, path):
        self.test_files = []
        self.success = True
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
                print(f"running test {test_name} - success")
            except AssertionError:
                print(f"running test {test_name} - failure")
                self.success = False

    def run(self):
        for test_file in self.test_files:
            self.run_single_file(test_file)

        if self.success:
            print(f"{colors.GREEN}tests succeeded{colors.RESET}")
        else:
            print(f"{colors.RED}tests failed{colors.RESET}")

if __name__ == "__main__":
    Runner(sys.argv[1]).run()
