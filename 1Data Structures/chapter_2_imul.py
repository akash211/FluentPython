l = [1, 2, 3]
print(id(l))

l *= 2
print(id(l))

t = (1, 2, 3)
print(id(t))

t *= 2
print(id(t))
# list remains same but new tuple is created


t = (1, 2, [30, 40])
try:
    t[2] += [50, 60] # This throws error still t gets changed
except TypeError as e:
    print(e)
print(t)

import dis  # used to generate bytecode for a code object
print(dis.dis('s[a] += b'))