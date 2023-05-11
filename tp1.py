from functools import reduce
import sys
import compression
import decompression
from Trie import Trie

output: str = ''
input: str = ''
extension: str = ''

if '-o' in sys.argv:
    o_index = sys.argv.index('-o') + 1
    output = sys.argv[o_index]

if '-c' in sys.argv:
    file_index = sys.argv.index('-c') + 1
    input = sys.argv[file_index]

    extension = '.z78'
    if output:
        output = output[0:output.rfind('.')] + extension
    else:
        output = input[0:input.rfind('.')] + extension
    compression.compress(input, output)

else:
    file_index = sys.argv.index('-x') + 1
    input = sys.argv[file_index]
    extension = '.txt'
    
    if output:
        output = output[0:output.rfind('.')] + extension
    else:
        output = input[0:input.rfind('.')] + extension
    decompression.decompress(input, output)
