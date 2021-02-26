#!/usr/bin/env python3
import sys
import os

binary = sys.argv[1]
filename = sys.argv[2]

for root, folder, file in os.walk(f'{os.getcwd()}'):
    if file == binary:
        print(f'deleting {file}')
        os.remove(file)

print(f'compiling {binary}')
os.system(f'gcc -o {binary} {filename}')
