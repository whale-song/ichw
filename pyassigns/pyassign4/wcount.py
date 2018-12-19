#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "WhaleSong"
__pkuid__  = "1800011751"
__email__  = "whalesong@pku.edu.cn"
"""

import sys
from urllib.request import urlopen

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    docfile = open('Desktop/cache/docs.txt', 'w')


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    # your code goes here
    # should anayze whether paras are right or not
