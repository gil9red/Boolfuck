"""
EN:
Interpreter language Boolfuck.
    + :	Flips the value of the bit under the pointer.
    , :	Reads a bit from the input stream, storing it under the pointer. The end-user types information using
        characters, though. Bytes are read in little-endian order; the first bit read from the character a, for
        instance, is 1, followed by 0, 0, 0, 0, 1, 1, and finally 0.
    ; :	Outputs the bit under the pointer to the output stream. The bits get output in little-endian order, the
        same order in which they would be input. If the total number of bits output is not a multiple of eight at
        the end of the program, the last character of output gets padded with zeros on the more significant end.
        If the end-of-file character has been input, outputs a zero to the bit under the pointer.
    < :	This moves the pointer left by one bit.
    > :	This moves the pointer right by one bit.
    [ :	If the value under the pointer is zero, jumps forward, just past the matching ] character.
    ] :	Jumps back to the matching [ character.


RU:
Интерпретатор языка Boolfuck.
    + : инвертировать бит в текущей ячейке;
    > : сдвинуть указатель данных на один бит вправо;
    < : сдвинуть указатель данных на один бит влево;
    [ : “начало цикла”;
    ] : “конец цикла”;
    , : прочитать бит из потока ввода;
    ; : записать бит в поток вывода.
"""

from collections import defaultdict
import sys
import argparse


__author__ = 'ipetrash'



def get_loops_block(source):
    begin_block = []
    blocks = {}
    for i, s in enumerate(source):
        if s is '[':
            begin_block.append(i)
        elif s is ']':
            b_i = begin_block.pop()  # b_i -- begin index
            blocks[i] = b_i
            blocks[b_i] = i
    return blocks


def execute(source):
    """
    EN:
    The function parses source code Boolfuck and execute it.

    RU:
    Функция выполняет разбор исходного кода Boolfuck и выполняет его.

    :param source: Исходный код
    :return:
    """

    i = 0  # A pointer to the row index in the code
    x = 0  # Cell index
    bf_bits = defaultdict(int)  # Dictionary, which is stored in the key index of the cell, and in the value - its value
    l = len(source)  # Number of code symbols
    loops_block = get_loops_block(source)
    bit_str = ''

    while i < l:
        s = source[i]

        if s is '>':  # Go to the next cell
            x += 1
        elif s is '<':  # Go to the previous cell
            x -= 1
        elif s is '+':  # Inverting bite in current cell
            bf_bits[x] = ~bf_bits[x] & 0b1
        elif s is ';':  # Printing the value of the current cell
            bit_str += str(bf_bits[x])
        elif s is ',':  # Enter a value in the current cell
			# TODO: operand , is not correct
            bf_bits[x] = int(input("Input = "))
        elif s is '[':  # Begin loop
            if not bf_bits[x]:  # If bf[x] == 0, then gets the index of the closing parenthesis
                i = loops_block[i]
        elif s is ']':  # End loop
            if bf_bits[x]:  # Если bf[x] != 0, then gets the index of the opening parenthesis
                i = loops_block[i]
        i += 1

    result = ''
    string_bites_byte = [bit_str[i:i+8] for i in range(0, len(bit_str), 8)]  # Splitting a string with 8 characters
    for bsb in string_bites_byte:
        bsb_be = bsb[::-1]  # Revert string. Transform to direction bits how in Big Endian
        s = chr(int(bsb_be, 2))  # Converting string with bits -> int -> char
        result += s
    print(result)


def create_parser():
    parser = argparse.ArgumentParser(description='Interpreter language Boolfuck.')
    parser.add_argument("path", help="Path to file")
    return parser


if __name__ == '__main__':
    parser = create_parser()

    if len(sys.argv) is 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        file_name = args.path
        source = open(file_name).read()
        execute(source)