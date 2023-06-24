# The collections.chainmap object in Python is a container that combines multiple mappings into a single, updatable view.
# It is often much faster than creating a new dictionary and running multiple update() calls.
# The class can be used to simulate nested scopes and is useful in templating.
# The ChainMap class is a subclass of the MutableMapping class.
# The ChainMap instance does not copy the input mappings, but holds references to them.
# Updates or insertions to a ChainMap only affect the first input mapping.

from collections import ChainMap
d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)

chain = ChainMap(d1, d2)
print(chain)
print(chain['a'])
print(chain['b'])
print(chain['c'])

chain['c'] = -1
print(d1)
print(d2)  # d2 is not changed
