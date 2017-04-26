import os
import sys


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def find_all_dirs(directory):
    for root,dirs,files in os.walk(directory):
        for dir in dirs:
            yield os.path.join(root,dir)

def print_all_files(directory):
    for file_path in find_all_files(directory):
        if ".pdf" in file_path:
          print file_path

def print_all_dirs(directory):
    for dir_path in find_all_dirs(directory):
        print dir_path

print_all_files(sys.argv[1])
#print_all_dirs(sys.argv[1])
