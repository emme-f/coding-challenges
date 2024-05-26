#!/usr/bin/env python3

import argparse
import sys


def count_bytes(text):
    return len(text.encode('utf-8'))

def count_lines(text):
    return len(text.splitlines())
    
def count_words(text):
    return sum(len(row.split())for row in text.splitlines())

def count_chars(text):
    return len(text)
 
def main():
    parser = argparse.ArgumentParser(description='Counting bytes, lines, words, characters of any text file')

    parser.add_argument('-c', '--bytes', action='store_true', help='Action to perform: -c for getting the size in bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Action to perform: -l for counting the num of rows in file')
    parser.add_argument('-w', '--words', action='store_true', help='Action to perform: -w for counting the num of words in file')
    parser.add_argument('-m', '--chars', action='store_true', help='Action to perform: -m for counting the num of characters in file')

    parser.add_argument('filename', nargs='?', default=None, help='The name of the file to process')
    
    args = parser.parse_args()

    if args.filename:
        text = open(args.filename, 'rb').read().decode()
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.print_help()
        sys.exit(1)

    if args.bytes:
        size_file_bytes = count_bytes(text=text)
        res_str = f"{size_file_bytes}"
    if args.lines:
        num_lines = count_lines(text=text)
        res_str = f"{num_lines}"
    if args.words:
        num_words = count_words(text=text)
        res_str = f"{num_words}"
    if args.chars:
        num_chars = count_chars(text=text)
        res_str = f"{num_chars}"
    
    if not args.bytes and not args.lines and not args.words and not args.chars:
        result = sorted([
            count_lines(filename=args.filename),
            count_bytes(filename=args.filename),
            count_words(filename=args.filename)
        ])
        res_str = f"{' '.join(map(str, result))}"
    
    if args.filename:
        res_str += f' {args.filename}'
    print(f"{' '*4}{res_str}")

if __name__ == "__main__":
    main()
