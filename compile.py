#!/usr/bin/env python3
import sys
import os

binary = sys.argv[1]
filename = sys.argv[2]

if binary == '-h':
    print('compile.py binary_name source_file_name')

for root, folder, file in os.walk(f'{os.getcwd()}'):
    if file == binary:
        print(f'deleting {file}')
        os.remove(file)

if len(sys.argv) > 3:
    extra_options = sys.argv[3]
    if extra_options != None:
        os.system(f'gcc -o {binary} {filename} {extra_options}')
    else:
        os.system(f'gcc -o {binary} {filename}')
