#!/usr/bin/env python3

import random
import os
import random

# Local packages
import templates # Code templates
import arg_parser # Argument parser

# Class for generating grammar based generator
class GrammarGen():
    file_to_write = os.path.join(os.path.dirname(__file__), "generator.py") # The generator to be generated
    grammar_file = os.path.join(os.path.dirname(__file__), "bin_grammar.g4") # Grammar file to generate generator
    tab = " " * 4 # To show tabs as spaces in generated python script

    # Check if 2 arrays has a common element (utility function)
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
    def generate(self, quiet):
        # Open grammar file
        with open (self.grammar_file, "r") as grammar:
            function_declaration = ""
            # Iterate trough lines
            for line in grammar:
                # Split the line into "words" and remove comments
                array = []
                for word in line.split():
                    if word != "///":
                        array.append(word)
                    else:
                        break
                # See if we need to delcare a new function
                if not self.common_data([":", "|", ";"], array):
                    this_function_name = array[0]
                    function_declaration += "%sdepth_counter = 0" % (self.tab)
                    # Define a function
                    function_declaration += "\n%sdef %s(self):" % (self.tab, this_function_name)
                    # Debug information
                    if not quiet:
                        function_declaration += "\n%sself.depth_counter += 1" % (self.tab * 2)
                        function_declaration += "\n%sprint(self.depth_counter)" % (self.tab * 2)
                    # Declare an empty test case
                    function_declaration += "\n%stest_case = \"\"" % (self.tab * 2)
                # If line is not empty after removing comments
                elif array != []:
                    # If it's not the end of the function
                    if not self.common_data([";"], array):
                        # If the line contains more elements, it has less probability to be generated
                        # (to avoid reaching maximum recursion depth)
                        function_declaration += "\n%sif not random.randint(0, %d):\n%stest_case = \"\"" % (self.tab * 2,
                        len(array), self.tab * 3)
                    # Iterate trough "words"
                    for element in array:
                        if element not in ["|", ":", ";"]:
                            # If element is one of these, it needs to be added to the test case
                            if element in ["'('", "')'"]:
                                # If there is an or, we need one more tab
                                function_declaration += "\n%stest_case += %s" % (self.tab * 3, element)
                            # Else (if it is a function)
                            else:
                                function_declaration += "\n%stest_case += self.%s()" % (self.tab * 3, element)
                        # If we reached the end of the function
                        elif element == ";":
                            # If test_case is empty we try it again
                            function_declaration += "\n%sif test_case == \"\":" % (self.tab * 2)
                            function_declaration += "\n%sreturn self.%s()" %(self.tab * 3, this_function_name)
                    # Return statement at the end of the function
                    # If we reached the end of the function, we already put a return statement
                    if not self.common_data([";"], array):
                        function_declaration += "\n%sreturn test_case" % (self.tab * 3)
            # Debug information
            if not quiet:
                print(function_declaration)
            return function_declaration

if __name__ == '__main__':
    args = arg_parser.parse_args()
    gram = GrammarGen()
    # Writing generator script
    with open(gram.file_to_write, "w") as file:
        # STARTER_FUNCTION defines which element of the grammar we want ot generate
        file.write("%s" % templates.class_template.format(GENERATED_FUNCTIONS = gram.generate(args.q),
        STARTER_FUNCTION = args.starter_element, TEST_COUNT = args.test_count, SEED = args.seed))
