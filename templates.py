#!/usr/bin/env python3

# Importing needed things, defining terminal elements of the grammar, defining generator and
# __main__, and declaring needed variables

class_template = '''#!/usr/bin/env python3

import os
import random
import sys
from templates import test_file

# Local packages
from arg_parser import _constants

class TestGenerator():
    random.seed({SEED})

{GENERATED_FUNCTIONS}

    def number(self):
        num = random.randint(_constants.min, _constants.max)
        return "(" + str(num) + ")"

    def operator(self):
        operator_array = ["+", "-", "*", "/", "%", "|", "&", "^"]
        return operator_array[random.randint(0, len(operator_array) - 1)]

    def generate(self):
        test_count = 0
        file_count = 1
        if not os.path.isdir(_constants.generated_folder):
            os.makedirs(_constants.generated_folder)
        while test_count != {TEST_COUNT}:
            with open (os.path.join(_constants.generated_folder, test_file.format(NO = file_count)), "w") as file:
                for i in range(0, {TEST_CASES_IN_A_FILE}):
                    test_count += 1
                    file.write(self.{STARTER_FUNCTION}())
                    if test_count != {TEST_CASES_IN_A_FILE} and test_count != {TEST_COUNT}:
                        file.write(\",\\n\")
                    else:
                        break
                file_count += 1

if __name__ == '__main__':
    generator = TestGenerator()
    generator.generate()
'''

test_file = '''testfile{NO}.js'''
