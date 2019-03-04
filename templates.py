class_template ='''#!/usr/bin/env python3

import os
import random

class TestGenerator():
    test_case = ""
    file_to_write = os.path.join(os.path.dirname(__file__), "testfile.js")
    depth_counter = 0 # TODO: count depth when a function calls another function (is not temrinal) 

{GENERATED_FUNCTIONS}

    def number(self):
        num = random.randint( - ((2 << 53) - 1),((2 << 53) - 1))
        return str(num)

    def operator(self):
        operator_array = ["+", "-", "*"]
        return operator_array[random.randint(0, len(operator_array) - 1)]

    def generate(self):
        with open (self.file_to_write, "w") as file:
            file.write(self.{STARTER_FUNCTION}())

if __name__ == '__main__':
    generator = TestGenerator()
    generator.generate()
'''
