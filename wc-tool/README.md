# Text File Analyzer

This Python script replicates the behavior of  provides functionality to count the number of bytes, lines, words, and characters in a given text file. It can be used from the command line and supports reading from both files and standard input.

## Features

- Count the number of bytes in a text file.
- Count the number of lines in a text file.
- Count the number of words in a text file.
- Count the number of characters in a text file.

## Requirements

- Python 3.x

## Installation

To make this script easily accessible from the command line, you can download it and place it in `/usr/local/bin`:

1. Download the script:
```curl https://raw.githubusercontent.com/mariof89/coding-challenges/master/wc-tool/ccwc.py -o ccwc.py```

2. Make the script executable:
```chmod +x ccwc.py```

3. Move the script to `/usr/local/bin`:
```sudo mv ccwc.py /usr/local/bin/ccwc```

You can now run the script using the command ccwc.

## Usage

### Command Line Arguments

- `-h`, `--help`: Show the help message and exit.
- `-c`, `--bytes`: Get the size of the file in bytes.
- `-l`, `--lines`: Count the number of lines in the file.
- `-w`, `--words`: Count the number of words in the file.
- `-m`, `--chars`: Count the number of characters in the file.

### Examples

#### Count bytes in a file
```ccwc -c example.txt```

#### Count lines in a file
```ccwc -l example.txt```

#### Count words in a file
```ccwc -w example.txt```

#### Count characters in a file
```ccwc -m example.txt```

#### Reading from standard input
You can also pipe input directly to the script:
```cat filename.txt | ccwc -w```
