from glob import glob as glob
import os
from main_decorator import main
from os.path import isdir as directory_exists
import argparse


@main
def main():
    parser = argparse.ArgumentParser(description='Calculating rectangle square')
    parser.add_argument('path', type=str, help='Input start directory for search')
    parser.add_argument('extension', type=str, help='Input file extension')

    try:
        args = parser.parse_args()
    except (SystemExit, ValueError, argparse.ArgumentError) as error:
        raise ValueError("You need enter only 2 string arguments: path and extension.") from error
    else:
        path = args.path
        extension = args.extension

        if path.endswith(('\\', '/')):
            path = path[:-1]

        if extension.startswith(os.extsep):
            extension = extension[1:]

        if not directory_exists(path):
            raise NotADirectoryError(f"Path {path} is incorrect.")

        if extension.count(os.extsep) > 0:
            raise ValueError(f"Incorrect extension: {extension} contains extra extseps.")

        for filename in glob(f"{path}/**/*{os.extsep}{extension}"):
            print(filename)
