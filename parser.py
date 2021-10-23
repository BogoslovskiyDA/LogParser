import glob
import os
import sys
import argparse
import re


def read_file(file, regular):
    '''
    Searching with Regular Expressions

    :param file: File path to read
    :param regular: Regular expression
    :return: None
    '''

    f = open(file, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        match = re.findall(fr'{regular}', line)
        if not match:
            continue
        print(match)
    f.close()


def create_arguments():
    '''
    Creating options for the terminal

    :return: argparse.ArgumentParser
    '''

    arg_par = argparse.ArgumentParser()
    arg_par.add_argument('-p', '--path')
    arg_par.add_argument('-f', '--find')
    return arg_par


if __name__ == '__main__':
    arg_par = create_arguments()
    argument = arg_par.parse_args(sys.argv[1:])
    files = glob.glob(os.path.join(argument.path, '*.txt'))
    if (files != []):
        for filename in files:
            read_file(filename, argument.find)
    else:
        read_file(argument.path, argument.find)
