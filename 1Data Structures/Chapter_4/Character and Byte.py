# From Python 3, str are now collection of unicode characters.
# This is a unicode string.
s = 'Hello, world!'
print(s)
# Unicode standard separates the identity of characters from specific byte representations.
# The identity of character (code point) is a number from 0 to 1,114,111(base 10).
# In unicode standard it is shown as 4 to 6 character hex digits with prefix "U+".
# For example for the letter A, the identity is U+0041.
# Python uses Unicode 13.0.0.
# The actual bytes that represent a character depend on the encoding in use.
# Encoding is an algorithm that convert code point to byte sequence and vice versa.
# The default encoding is UTF-8. Letter A is encoded as \x41 and takes one byte.
# In encoding UTF-16LE, letter A is encoded as \x41\x00 and takes two bytes.
# Euro sign in UTF-8 is \xe2\x82\xac while in UTF-16LE it is \xac\x20.

# byte literals has a b prefix.
print('A'.encode('utf8'))
print(bytes('A', encoding='utf_8'))
print('A'.encode('utf8')[0])
print('A'.encode('utf_16-le'))
print('A'.encode('utf_16-le')[0])
print('€'.encode('utf8'))
print('€'.encode('utf_16-le'))
print('€'.encode('utf_16-le')[0])
print('€'.encode('utf_16-le')[1])

coded = 'café'.encode('utf8')
print(coded)  # Total 5 bytes
print(coded.decode('utf8'))

print('c'.encode('utf8'))
print('a'.encode('utf8'))
print('f'.encode('utf8'))
print('é'.encode('utf8'))

# Python 3 has immutable bytes and mutable bytearray.
# each item in bytes or bytearray is an integer between 0 and 255.

cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[1])
print(cafe[2])
print(cafe[3])
print(cafe[4])
print(cafe[:1])  # for most sequence types in Python, 1 item is not the same as a slice of length 1. so 0 and :1 are different.
print(cafe[:2])
print(cafe[:3])
print(cafe[:4])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[0])
print(cafe_arr[1])
print(cafe_arr[2])
print(cafe_arr[3])
print(cafe_arr[-1:])  # slice of bytearray is also bytearray

# Although binary sequences are really sequences of integers, their literal notation reflects the fact that ASCII text is often embedded in them.
# Therefore, four different displays are used, depending on each byte value:
# 1. For bytes with decimal codes 32 to 126—from space to ~ (tilde)—the ASCII character itself is used.
# 2. For bytes corresponding to tab, newline, carriage return, and \, the escape sequences \t, \n, \r, and \\ are used.
# 3. If both string delimiters ' and " appear in the byte sequence, the whole sequence is delimited by ', and any ' inside are escaped as \'.3
# 4. For other byte values, a hexadecimal escape sequence is used (e.g., \x00 is the null byte).

print(bytes([1, 2, 3, 4]))
print(bytes((1, 2, 3, 4)))
print(bytes({1, 2, 3, 4}))

