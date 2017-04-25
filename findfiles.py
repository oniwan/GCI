import os
import sys


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


def print_all_files(directory):
    for file in find_all_files(directory):
        print file

print_all_files(sys.argv[1])
