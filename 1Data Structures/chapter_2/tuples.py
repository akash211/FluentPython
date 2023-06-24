"""
## Two benefits of tuple
Clarity: When you see a tuple in code, you know its length will never change.

Performance: A tuple uses less memory than a list of the same length, and it allows Python to do some optimizations.

However, be aware that the immutability of a tuple only applies to the references contained in it.
References in a tuple cannot be deleted or replaced. But if one of those references points to a mutable object,
and that object is changed, then the value of the tuple changes.
"""

a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a == b)
b[-1].append(99)  # even if b is tuple,
print(a == b)  # its value changes because it refers to a list which changed
print(b)

# So tuples should only have hashable objects.
# Hashable objects are those whose values does not change
# using hash method we can find if an element is hashable or not


def hash_function(inp):
    try:
        return f"{inp} is hashable and hash value is {hash(inp)}"
    except TypeError:
        return f"{inp} is Not hashable"


print(hash_function((1, 0)))
print(hash_function([1, 0]))
print(hash_function((1, 0, [1, 2])))
print(hash_function((1, 0, (1, 2))))

