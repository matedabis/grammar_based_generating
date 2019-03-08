#!/usr/bin/env python3
import sys
import argparse
import os

# Default values and constants
class _constants:
    default_test_count = 10     # Default number of test cases to be generated
    default_seed = 9999         # Default seed for random
    max = (1 << 53) - 1         # The max value of random number (See also Number.MAX_SAFE_INTEGER)
    min = - 1 * max             # The min value of random number (See also Number.MIN_SAFE_INTEGER)
    test_cases_in_a_file = 700  # Number of test cases in a test file
    generated_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated")

# Argument parser
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--starter-element", help = "Element of grammar to generate", required = True)
    parser.add_argument("--test-count", help = "Number of tests to generate", type = int,
    default = _constants.default_test_count)
    parser.add_argument("--seed", help = "Seed value used while generating random number", type = int,
    default = _constants.default_seed)
    parser.add_argument("-q", help = "Does not print any output", action='store_true')

    # If there are no arguments, print help and exit with exit code: 1
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()
