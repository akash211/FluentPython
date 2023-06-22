# The standard library offers a rich selection of sequence types implemented in C:

# 1. Container sequences
# Can hold items of different types, including nested containers. Some examples: list, tuple, and collections.deque.
# A container sequence holds references to the objects it contains, which may be of any type,

# 2. Flat sequences
# Hold items of one simple type. Some examples: str, bytes, and array.array.
# A flat sequence stores the value of its contents in its own memory space, not as distinct Python objects.

from collections import abc

print(issubclass(str, abc.Sequence))

print(issubclass(list, abc.MutableSequence))
