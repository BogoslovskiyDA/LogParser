import glob
import sys
import argparse
import re
from progress.bar import IncrementalBar


def read_file(in_file, regular, out_file):
    '''
    Searching with Regular Expressions

    :param in_file: File path to read
    :param regular: Regular expression
    :param out_file: File to write
    :return: None
    '''

    f = open(in_file, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        if re.findall(fr'{regular}', line):
            out_file.write(line)
    f.close()


def create_arguments():
    '''
    Creating options for the terminal

    :return: argparse.ArgumentParser
    '''

    arg_par = argparse.ArgumentParser(add_help=False)
    arg_par.add_argument('-h', '--help', action='help', help='Print this help message and exit')
    arg_par.add_argument('-p', '--path', help='Read file/folder by specified PATH (RegEx)')
    arg_par.add_argument('-f', '--find', help='Search strings (RegEx)', metavar='REGEX')
    arg_par.add_argument('-o', '--output', default='output.txt', help=f'File to write. Default=output.txt')
    return arg_par.parse_args(sys.argv[1:])


if __name__ == '__main__':
    argument = create_arguments()
    files = glob.glob(fr'{argument.path}')
    out_file = open(argument.output, 'w')
    if files:
        bar = IncrementalBar('Progress', max=len(files))
        bar.start()
        for filename in files:
            read_file(filename, argument.find, out_file)
            bar.next()
        bar.finish()
    out_file.close()
