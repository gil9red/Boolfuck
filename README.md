Interpreter Boolfuck.
===========

####EN:
Interpreter language Boolfuck.

| Character |                       Meaning                  |
|-----------|------------------------------------------------|
|    +      | Flips the value of the bit under the pointer.  |
|    >      | This moves the pointer right by one bit.       |
|    <      | This moves the pointer left by one bit.        |
|    [      | If the value under the pointer is zero, jumps forward, just past the matching ] character. |
|    ]      | Jumps back to the matching [ character.        |
|    ,      | Reads a bit from the input stream, storing it under the pointer. The end-user types information using characters, though. Bytes are read in little-endian order; the first bit read from the character a, for instance, is 1, followed by 0, 0, 0, 0, 1, 1, and finally 0.                 |
|    ;      | Outputs the bit under the pointer to the output stream. The bits get output in little-endian order, the same order in which they would be input. If the total number of bits output is not a multiple of eight at the end of the program, the last character of output gets padded with zeros on the more significant end. If the end-of-file character has been input, outputs a zero to the bit under the pointer.     |


####RU:
Интерпретатор языка Boolfuck.

|  Команда  |      Описание команды                          |
|-----------|------------------------------------------------|
|    +      | инвертировать бит в текущей ячейке;            |
|    >      | сдвинуть указатель данных на один бит вправо;  |
|    <      | сдвинуть указатель данных на один бит влево;   |
|    [      | “начало цикла”;                                |
|    ]      | “конец цикла”;                                 |
|    ,      | прочитать бит из потока ввода;                 |
|    ;      | записать бит в поток вывода.                   |
