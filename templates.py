#!/usr/bin/env python3

# Importing needed things, defining terminal elements of the grammar, defining generator and
# __main__, and declaring needed variables

class_template ='''#!/usr/bin/env python3

import os
import random
import sys

# Local packages
from arg_parser import _constants

class TestGenerator():
    file_to_write = os.path.join(os.path.dirname(__file__), "testfile.js")
    random.seed({SEED})

{GENERATED_FUNCTIONS}

    def number(self):
        num = random.randint(_constants.min, _constants.max)
        return str(num)

    def operator(self):
        operator_array = ["+", "-", "*", "/", "%", "|", "&", "^"]
        return operator_array[random.randint(0, len(operator_array) - 1)]

    def generate(self):
        with open (self.file_to_write, "w") as file:
            for i in range(0, {TEST_COUNT}):
                file.write(self.{STARTER_FUNCTION}())
                if i != {TEST_COUNT} - 1:
                    file.write(\",\\n\")

if __name__ == '__main__':
    generator = TestGenerator()
    generator.generate()
'''
