#!/usr/bin/env python3

import argparse
import os
import re


def count_bytes(filename):
    return os.path.getsize(filename)

def count_lines(filename):
    return sum(1 for _ in open(filename))

def count_words(filename):
    return sum(len(row.split())for row in open(filename))

def count_chars(filename):
    with open(filename, 'r') as file:
        chars = 0
        for line in file.readlines():
            chars += len(line)
        return chars
        
        return len(adjusted_text)
    return f"{sum(len(row)for row in open(filename))} {filename}"
 
def main():
    parser = argparse.ArgumentParser(description='Process some files')

    #group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('-c', '--bytes', action='store_true', help='Action to perform: -c for getting the size in bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Action to perform: -l for counting the num of rows in file')
    parser.add_argument('-w', '--words', action='store_true', help='Action to perform: -l for counting the num of rows in file')
    parser.add_argument('-m', '--chars', action='store_true', help='Action to perform: -l for counting the num of rows in file')

    #group.add_argument('action', choices=['-t', '--truncate'], help='Action to perform: -c for countg word')
    
    parser.add_argument('filename', help='The name of the file to process')
    
    args = parser.parse_args()

    if args.bytes:
        size_file_bytes = count_bytes(filename=args.filename)
        res_str = f"{size_file_bytes} {args.filename}"
    if args.lines:
        num_lines = count_lines(filename=args.filename)
        res_str = f"{num_lines} {args.filename}"
    if args.words:
        num_words = count_words(filename=args.filename)
        res_str = f"{num_words} {args.filename}"
    if args.chars:
        num_chars = count_chars(filename=args.filename)
        res_str = f"{num_chars} {args.filename}"
    if not args.bytes and not args.lines and not args.words and not args.chars:
        result = sorted([
            count_lines(filename=args.filename),
            count_bytes(filename=args.filename),
            count_words(filename=args.filename)
        ])
        res_str = f"{' '.join(map(str, result))} {args.filename}" 
    print(f"{' '*4}{res_str}")
if __name__ == "__main__":
    main()
