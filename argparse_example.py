#! usr/bin/env python

import argparse

parser = argparse.ArgumentParser()


parser.add_argument('-p', '--print', action='store_true', help='prints out a different message')

args = parser.parse_args()


if args.print:
    print('a message')

else:
    print('nothing')
