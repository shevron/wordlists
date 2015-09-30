# Word Lists
## a repository of free-to-use accessible lists of words

What is this?
-------------
This is a repository I started to collect organized human-and-computer
accessible files containing lists of words.

In addition to files containing lists of words (in the `lists` folder),
this project also houses some scripts and utilities in various programming
languages to access and manage these lists.

Why?
----
Because lists of words are useful in many ways. You can use them to
generate memorable hostnames, passphrases, version names etc. I was surprised
not to find such easy-to-consume list when I needed it, so I decided to create
one and share it for the benefit of everyone else.

I'm sure this will prove useful to me and to others in ways I have not
imagined.

Word List Files
---------------
The lists of words are stored in the `lists` folder, each category of words
in its own file. The file format is designed to be kind-of-human-readable, but
at the same time have some features that make it randomly-accessible by
software.

Each file contains a single categorized list of words. Words should not repeat
more than once in each file - in other words, within each file, each word is
unique. However, a word may show up in multiple files.

### File Format

- Word list files are plain-text files encoded in UTF-8.
- Lines are separated by a standard UNIX LF character "`\n`" (ASCII `0x0a`)
- The first line of the file is a "header" line containing metadata information
  about the file (more on that further on)
- All other lines in the file are actual words, each word (or phrase) in its
  own line
- Each word is end-padded with space (ASCII `0x20`) characters so that the
  length of all lines in a file (except for the first line) in bytes is equal

### Header Line Format

- The header line is composed of several pipe symbol (`|`, ASCII `0x7c`)
  separated fields
- The 1st field is exactly 2-bytes long, and contains two hexadecimal digits
  in ASCII representation specifying the file format version, (currently `01`).
  This is the only future-proof element in the file format, and hence needs to
  be of fixed length.
- The 2nd field contains a friendly name of the list, for example
  describing the category all words in the list belong to (usually this
  corresponds with the file name)
- The 3rd field contains the number of words in the list, in decimal notation
- The 4th field contains the exact length in bytes (not characters! UTF8,
  remember?) of each line in the file, starting from the second line, including
  the ending LF character. This designates the amount of space padding added
  to words when the list was built.

The 3rd and 4th header fields together can be used to treat the list file as a
random-access array of words without reading the entire list to memory.

### Example

Here is an example of a minimal word list file. Assume dots represent a space
character:

    01|Solar System Planets|8|8
    Mercury
    Venus..
    Earth..
    Mars...
    Jupiter
    Saturn.
    Uranus.
    Neptune


In this example, the header line teaches us that:

- This is a version 01 file format
- It contains a list of "Solar System Planets"
- It has exactly 8 items
- Each item is 8 bytes long

You can also notice that shorter words have been zero-padded so that each line
is *exactly* 8 bytes including the trailing LF character. For example, 'Mars'
was suffixed with 3 space characters.

This format is not very space-efficient, but as mentioned when read from disk
or over a network protocol that allows partial / positional reads (such as
HTTP), it allows for fast and memory / CPU efficient random access.

License and Copyright
---------------------
The software in this repository is distributed of the MIT license, readable in
the LICENSE.md file, and is copyright (c) 2015 Shahar Evron.

The list of words in the files under the `lists` directory are Public Domain.
They are just words.
