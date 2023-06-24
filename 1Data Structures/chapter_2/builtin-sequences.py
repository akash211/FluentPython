# The standard library offers a rich selection of sequence types implemented in C:

# 1. Container sequences
# Can hold items of different types, including nested containers. Some examples: list, tuple, and collections.deque.
# A container sequence holds references to the objects it contains, which may be of any type,
# Some objects contain references to other objects; these are called containers.

# I used the term “container sequence” to be specific, because there are containers in Python that are not sequences,
# like dict and set. Container sequences can be nested because they may contain objects of any type, including their own type

# 2. Flat sequences
# Hold items of one simple type. Some examples: str, bytes, and array.array.
# A flat sequence stores the value of its contents in its own memory space, not as distinct Python objects.
# flat sequences are sequence types that cannot be nested because they only hold simple atomic types like integers, floats, or characters.
# I adopted the term flat sequence because I needed something to contrast with container sequence.

from collections import abc

print(issubclass(str, abc.Sequence))

print(issubclass(list, abc.MutableSequence))

l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
print(sorted(l, key=int))
print(sorted(l, key=str))



