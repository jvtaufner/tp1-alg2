from functools import reduce
import sys
import globals
from Trie import Trie


def decompress(input: str, output: str):
    inputFile = open(input, 'rb')

    values: list[str] = ['']
    codeSize = int.from_bytes(inputFile.read(1), globals.ORDER)
    code = int.from_bytes(inputFile.read(codeSize), globals.ORDER)
    char = inputFile.read(globals.CHAR_SIZE)

    string: str = ''
    out: str = ''

    while char:
        char = chr(ord(char))
        string = values[code] + char
        out += string
        values.append(string)
        codeSize = int.from_bytes(inputFile.read(1), globals.ORDER)
        code = int.from_bytes(inputFile.read(codeSize), globals.ORDER)
        char = inputFile.read(globals.CHAR_SIZE)

    string = values[code]
    out += string

    output_file = open(output, 'w', encoding='utf-8')
    output_file.write(out)

    inputFile.close()
    output_file.close()