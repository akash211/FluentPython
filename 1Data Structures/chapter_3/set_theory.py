# A set is a collection of unique objects. A basic use case is removing duplication
# Set elements must be hashable. The set type is not hashable, so you can’t build a set with nested set instances.
# But frozenset is hashable, so you can have frozenset elements inside a set.
# Set is an unordered collection of items.
# Set is mutable.
# set implements many set operations like union (a |b), intersection (a & b), difference (a - b), symmetric difference (a ^ b).
# there’s no literal notation for the empty set, so we must remember to write set().
# Literal set syntax like {1, 2, 3} is both faster and more readable than calling the constructor (e.g., set([1, 2, 3])).
# The latter form is slower because, to evaluate it, Python has to look up the set name to fetch the constructor, then build a list, and finally pass it to the constructor.
# In contrast, to process a literal like {1, 2, 3}, Python runs a specialized BUILD_SET bytecode.
# There is no special syntax to represent frozenset literals—they must be created by calling the constructor.
# Adding elements to a set may change the order of existing elements.

haystack = set(range(1000))
needle = {12, 45, 56, 22, 24535, 77777777, 4326464756745867}
print(len(needle & haystack))
print(len(needle.intersection(haystack)))  # same as above

print(frozenset(range(10)))
print(frozenset(range(10)) == set(range(10)))
print(frozenset(range(10)) == set(range(9, -1, -1)))

from unicodedata import name
print({name(chr(i), '') for i in range(32, 256) })
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})
print({chr(i) for i in range(32, 256) if 'LETTER' in name(chr(i), '')})


