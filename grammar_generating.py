#!/usr/bin/env python3

import random
import subprocess
import os
import re
import random

# Local packages
import templates # Code templates

# Class for generating grammar based generator
class GrammarGen():
    file_to_write = os.path.join(os.path.dirname(__file__), "generator.py") # The generator to be generated
    grammar_file = os.path.join(os.path.dirname(__file__), "bin_grammar.g4") # Grammar file to generate generator
    tab = " " * 4 # To show tabs as spaces in generated python script

    # Check if 2 arrays has a common element
    def common_data(self, list1, list2):
        result = False
        # traverse in the 1st list
        for x in list1:
            # traverse in the 2nd list
            for y in list2:
                # if one common
                if x == y:
                    result = True
                    return result
        return result

    # Generate function declarations according to the grammar
    def generate(self):
        # Open grammar file
        with open (self.grammar_file, "r") as grammar:
            function_declaration = ""
            # Iterate trough lines
            for line in grammar:
                print(line.split())
                # See if we need to delcare a new function
                if not self.common_data(["///", ":", "|", ";"], line.split()):
                    function_declaration += "%sdef %s(self):" % (self.tab, line.strip("\n"))
                    function_declaration += "\n%stest_case = \"\"" % (self.tab * 2)
                # If line is not a comment
                elif not self.common_data(["///"], line.split()):
                    # Split the line into "words"
                    array = line.split()
                    # If there is an "or"
                    if self.common_data("|", array):
                        function_declaration += "\n%sif(random.randint(0, 1)):\n%stest_case = \"\"" % (self.tab * 2,
                        self.tab * 3)
                    # Iterate trough "words"
                    for element in array:
                        if element not in ["|", ":", ";"]:
                            # If element is one of these, it needs to be added to the test case
                            if element in ["'('", "')'"]:
                                # If there is an or, we need one more tab
                                if self.common_data("|", array):
                                    function_declaration += "\n%stest_case += %s" % (self.tab * 3, element)
                                else:
                                    function_declaration += "\n%stest_case += %s" % (self.tab * 2, element)
                            # Else (if it is a function)
                            else:
                                if self.common_data("|", array):
                                    function_declaration += "\n%stest_case += self.%s()" % (self.tab * 3, element)
                                else:
                                    function_declaration += "\n%stest_case += self.%s()" % (self.tab * 2, element)
                        # If we reached the end of the function
                        elif element == ";":
                            # Return statement at the end of the function
                            function_declaration += "\n%sreturn test_case" % (self.tab * 2)
            print(function_declaration)
            return function_declaration

    def CONTENT(self):
        self.output_string += rstr.xeger(r'[a-zA-Z0-9_][a-zA-Z0-9_ \t]*')

if __name__ == '__main__':
    gram = GrammarGen()
    with open(gram.file_to_write, "w") as file:
        file.write("%s" % templates.class_template.format(GENERATED_FUNCTIONS = gram.generate(),
        STARTER_FUNCTION = "expression"))
