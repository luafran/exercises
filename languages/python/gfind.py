import os
import fnmatch
import gzip, bz2
import re
import sys
import unittest
import argparse

# parser = argparse.ArgumentParser(description='grep and find')
# parser.add_argument("dir")
# parser.add_argument()

# args = parser.parse_args()

# print args.dir


class NullFileIter:

    def __init__(self):
        pass

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration()


class NullFile:

    def __init__(self):
        self.my_iter = NullFileIter()
        pass

    def __iter__(self):
        return self.my_iter


# A function that generates files that match a given filename pattern
def gen_find(file_pattern, top):
    try:
        for path, dir_list, file_list in os.walk(top):
            for file_name in fnmatch.filter(file_list, file_pattern):
                yield os.path.join(path, file_name)
    except Exception as ex:
        print 'Exception in find: ' + ex.message


# Takes a sequence of file_names as input and yields a sequence of file
# objects that have been suitably open
def gen_open(file_names):
    for name in file_names:
        try:
            if name.endswith(".gz"):
                yield gzip.open(name)
            elif name.endswith(".bz2"):
                yield bz2.BZ2File(name)
            else:
                yield open(name)
        except IOError as ex:
            sys.stderr.write("Can't open {0}: {1}\n".format(name, ex.strerror))
            yield NullFile()


# Grep a sequence of lines that match a re pattern
def gen_grep(pattern, lines):
    patc = re.compile(pattern)
    for line in lines:
        if patc.search(line):
            yield line


# Concatenate multiple generators into a single sequence
def gen_cat(sources):
    try:
        for s in sources:
            for item in s:
                yield item
    except Exception as ex:
        print 'Exception: ', ex.message


def lines_from_dir(file_pattern, dir_name):
    names = gen_find(file_pattern, dir_name)
    files = gen_open(names)
    lines = gen_cat(files)
    return lines


if __name__ == '__main__':
    lines = lines_from_dir('*.txt', 'test-traverse-dirs')
    match_lines = gen_grep(r'some text', lines)
    for line in match_lines:
        print line,


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