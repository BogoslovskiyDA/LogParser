import glob
import os
import sys
import argparse


def read_file(file):
    f = open(file, 'r')
    print(f.readlines())
    f.close()


def read_arguments():
    arg_par = argparse.ArgumentParser()
    arg_par.add_argument('-p', '--path')
    return arg_par


if __name__ == '__main__':
    arg_par = read_arguments()
    path = arg_par.parse_args(sys.argv[1:])
    files = glob.glob(os.path.join(path.path, '*.txt'))
    if (files != []):
        for filename in files:
            read_file(filename)
    else:
        read_file(path.path)
