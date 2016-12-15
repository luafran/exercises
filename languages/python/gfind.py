import os
import fnmatch
import gzip, bz2
import re
import unittest
import argparse

# parser = argparse.ArgumentParser(description='grep and find')
# parser.add_argument("dir")
# parser.add_argument()

# args = parser.parse_args()

# print args.dir


def grep_in_lines(lines, pattern, ignore_case=False):

    match_lines = []
    c_pattern = re.compile(pattern)

    flags = 0
    if ignore_case:
        flags = re.IGNORECASE
    try:

        for line in f:
            if re.search(c_pattern, line, flags):
                match_lines.append(line.strip())

    except IOError as ex:
        print ex.message

    return match_lines


def gfind(dir, file_types=None, substring=None, pattern=None):

    for root, dirs, files in os.walk(dir):
        for file_name in files:
            full_path = os.path.join(root, file_name)

            if substring in file_name:
                print full_path
                if pattern is not None:
                    with open(file_name, 'r') as f:
                        for line in f:
                            match_lines = grep_in_file(full_path, pattern)
                    print match_lines


def gen_find(file_pattern, top):
    for path, dir_list, file_list in os.walk(top):
        for file_name in fnmatch.filter(file_list, file_pattern):
            yield os.path.join(path, file_name)


def gen_open(filenames):
    for name in filenames:
        if name.endswith(".gz"):
            yield gzip.open(name)
        elif name.endswith(".bz2"):
            yield bz2.BZ2File(name)
        else:
            yield open(name)

# Example use

if __name__ == '__main__':
    file_names = gen_find("*.py", ".")
    files = gen_open(file_names)
    for f in files:
        print f


class TestGFind(unittest.TestCase):

    def search_substring_in_filename_no_pattern(self):

        in_dir = '.'
        substring = 'gfind'
        gfind(in_dir, substring=substring)

    def search_substring_in_filename_pattern(self):
        in_dir = '.'
        substring = 'gfind'
        pattern = 'gfind'
        gfind(in_dir, substring=substring, pattern=pattern)

    def test_search_substring_in_filename_pattern_case(self):
        in_dir = '.'
        substring = 'gfind'
        pattern = 'GFIND'
        gfind(in_dir, substring=substring, pattern=pattern)