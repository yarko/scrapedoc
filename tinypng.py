#!/bin/env python
#
# this is from http://garethrees.org/2007/11/14/pngcrush/
#
import zlib
import codecs
import struct

def chunk(type, data):
    return (struct.pack('>I', len(data)) + type + data
    + struct.pack('>i', zlib.crc32(type + data)))
    
png = ('\x89PNG\r\n\x1A\n'
   + chunk('IHDR', struct.pack('>IIBBBBB', 1, 1, 1, 0, 0, 0, 0))
   + chunk('IDAT', zlib.compress(struct.pack('>BB', 0, 0)))
   + chunk('IEND', ''))
# len(png)
# OUT: 67
with open('1x1.png', 'w') as f:
    f.write(png)
    

