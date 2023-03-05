#!/usr/bin/env python3

"""
Validates schema files (e.g. OcConfigurationLib.c) for being sorted.
"""


import re
import sys

if len(sys.argv) < 2:
    print('Pass file to check')
    sys.exit(-1)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    prev = ''
    content = [line.strip() for line in f.readlines()]
    for index, line in enumerate(content):
        if line == 'OC_SCHEMA':
            print('Checking schema {}'.format(re.match(r'^\w+', content[index + 1])[0]))
            prev = ''
            continue
        if x := re.search(r'"([^"]+)"', line):
            if x[1] < prev:
                print(f'ERROR: {prev} precedes {x[1]}')
                sys.exit(1)
            prev = x[1]
