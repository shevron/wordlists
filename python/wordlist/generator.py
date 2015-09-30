"""
Build a wordlist data file from a file containing a delimited list of words

Run `python -m wordlist.generator --help` for usage information
"""

import argparse
from . import FORMAT_VERSION


def analyze_list(wordlist):
    """
    Analyze a list of words and return a tuple containing (number of items, longest word in bytes)

    :param wordlist: list of words
    :return: tuple containing (number of items, longest word in bytes)
    """
    longest = 0
    count = 0
    for word in wordlist:
        word = word.strip()
        count += 1
        longest = max(longest, len(word))

    return count, longest


def generate_list(wordlist, title, count, longest, version=FORMAT_VERSION, separator='\n'):
    """
    List of words file generator

    This is a generator consuming an input list of words and yielding a new list
    in the proper word list format

    :param wordlist: Input list / file (iterable)
    :param title: List name / title
    :param count: Number of items in list
    :param longest: Longest line width in bytes
    :param version: File version
    :param separator: Line separator
    :return:
    """
    header = "{:02x}|{}|{}|{}{}".format(version, title, count, longest + 1, separator)
    yield header

    for word in wordlist:
        assert len(word) <= longest, "Expecting all words to be up to %d bytes, '%s' is longer" % (longest, word)
        yield "{: <{padding}}{}".format(word, separator, padding=longest)


def _file_read_items(infile, separator='\n'):
    """
    Read items from file based on a custom separator

    This is different from file.readline() in that it allows custom separators

    Adapted from an answer to
    http://stackoverflow.com/questions/16260061/reading-a-file-with-a-specified-delimiter-for-newline

    :param infile:
    :param separator:
    :return:
    """
    buf = ""
    while True:
        while separator in buf:
            pos = buf.index(separator)
            yield buf[:pos]
            buf = buf[pos + len(separator):]
        chunk = infile.read(4096)
        if not chunk:
            yield buf
            break
        buf += chunk


def _main():
    """
    Main function if run directly
    """
    import sys

    parser = argparse.ArgumentParser(description="Create a wordlist file from delimited list of words")
    parser.add_argument('-o', '--output', required=False, type=argparse.FileType('w'),
                        help='Output file (if omitted, STDOUT is used)', default=sys.stdout)
    parser.add_argument('-t', '--title', required=True, help='List title')
    parser.add_argument('-s', '--separator', required=False,
                        help="Input list separator (default: LF)", default="\n")
    parser.add_argument('input', type=argparse.FileType('r'), help='Input file')

    args = parser.parse_args()

    with args.input as infile, args.output as outfile:
        items, longest = analyze_list(_file_read_items(infile, args.separator))
        infile.seek(0)
        for outline in generate_list(_file_read_items(infile, args.separator), args.title, items, longest):
            outfile.write(outline)


if __name__ == '__main__':
    _main()

