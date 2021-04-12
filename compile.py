#!/usr/bin/env python3
import sys
import os

option = sys.argv[1]

if binary == '-h':
    print('compile.py option_name')

for root, folder, file in os.walk(f'{os.getcwd()}'):
    if file == binary:
        print(f'deleting {file}')
        os.system('make clean')

print(f'compiling {binary}')
if len(sys.argv) > 2:
    os.system(f"make {option}")
else:
    os.system('make')
