from collections import abc

my_dict = {}
print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))

# An object is hashable if it has a hash code which never changes during its lifetime (it needs a __hash__() method),
# and can be compared to other objects (it needs an __eq__() method).
# Hashable objects which compare equal must have the same hash code
# Numeric types and flat immutable types str and bytes are all hashable.
# Container types are hashable if they are immutable and all contained objects are also hashable.
# A frozenset is always hashable, because every element it contains must be hashable by definition.
# A tuple is hashable only if all its items are hashable.

