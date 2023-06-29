# Byte Order Mark (BOM)

A Byte Order Mark (BOM) is the character at code point FEFF. It is
used to denote how the data in a Unicode, Unicode big endian, or UTF-8 file is
encoded. In Unicode (little endian), the first byte of the file is FF, and the
second byte is FE. In Unicode big endian, the first byte of the file is FE, and
the second byte is FF. In UTF-8, the first byte of the file is EF, the second
byte is BB and the third byte is BF.