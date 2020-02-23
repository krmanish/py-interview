#! /usr/bin/env python
import sys
import argparse

def showFib():
    parser = argparse.ArgumentParser('Find Fibonancii Series')
    parser.add_argument('-a', '--array', type=str, action='store', help='Enter comma separated numbers', required=True)
    args = parser.parse_args()
    
    arr = list(map(lambda x: int(x), args.array.split(',')))
    length = len(arr) + 1 
    num = length * (length + 1) / 2 -  sum(arr)

    print('Missing Number is.. ')
    print('\t' , num)

            
if __name__ == '__main__':
    sys.exit(showFib())

