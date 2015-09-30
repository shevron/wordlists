"""
Wordlist Python module
"""

FORMAT_VERSION = 1


class WordlistFile(object):

    def __init__(self, source):
        """
        Create a new Wordlist object

        :param source: Source list: an open file-like object or file name to open
        """
        if isinstance(source, basestring):
            self._source = open(source)
        else:
            self._source = source

        self.version = 0
        self.title = None

        self._item_count = 0
        self._item_size = 0
        self._zero_pos = 0
        self._parse_header()

    def _parse_header(self):
        firstline = self._source.readline().strip()
        fields = firstline.split('|')
        self.version = int(fields[0])

        # Some input format validation
        if self.version != FORMAT_VERSION:
            raise RuntimeError("Unparsable wordlist file format version: %s" % fields[0])
        if len(fields) != 4:
            raise RuntimeError("Unexpected number of fields in file header")

        self.title = fields[1]
        self._item_count = int(fields[2])
        self._item_size = int(fields[3])
        self._zero_pos = self._source.tell()

    def _get_item_in_pos(self, pos):
        self._source.seek(pos)
        item = self._source.read(self._item_size).strip()
        return item

    def __len__(self):
        return self._item_count

    def __getitem__(self, item):
        if item > self._item_count - 1:
            raise IndexError("Unknown index: %d; Wordlist contains %d items", item, len(self))
        pos = self._zero_pos + self._item_size * item
        return self._get_item_in_pos(pos)

    def __repr__(self):
        """
        Get the string representation of this object

        :return: str
        """
        return "<%s %s items=%d>" % (self.__class__.__name__, self.title, len(self))
