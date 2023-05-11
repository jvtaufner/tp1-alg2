from functools import reduce
import sys
from Trie import Trie
import globals


def bytesNum(num: int) -> int:
    x = 0
    while num > 2**x:
        x += 1
    x = x // globals.BYTE_SIZE + 1
    return x

def compressionGenerator(accumulators: tuple[Trie, bytes, str], char: str):
    dictionary = accumulators[0]
    out = accumulators[1]
    string = accumulators[2]

    if dictionary.find(string + char) > -1:
        string = string + char

    else:
        code = dictionary.find(string)
        codeSize = bytesNum(code)
        charNum = ord(char)

        out += codeSize.to_bytes(1, globals.ORDER) + code.to_bytes(
            codeSize, globals.ORDER) + charNum.to_bytes(globals.CHAR_SIZE, globals.ORDER)

        dictionary.insert(string + char)
        string = ''

    return (dictionary, out, string)


def compress(input: str, output: str):
    inputFile = open(input, 'r', encoding='utf-8')
    fullIn: str =inputFile.read()
    inputFile.close()

    dictionary, out, string = reduce(
        compressionGenerator, fullIn, (Trie(), bytes(), ''))

    code = dictionary.find(string)
    codeSize = bytesNum(code)
    out += codeSize.to_bytes(1, globals.ORDER) + code.to_bytes(codeSize, globals.ORDER)

    outputFile = open(output, 'wb')
    outputFile.write(out)
    outputFile.close()
