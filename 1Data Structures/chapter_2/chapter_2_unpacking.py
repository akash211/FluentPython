print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))  # divmod requires 2 arguments. if we just give t, it complains.

a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)


def fun(a, b, c, d, *rest_):
    return a, b, c, d, rest_


print(fun(*[1, 2], 3, *range(4, 7)))

print({*range(4), 4, *(5, 6, 7)})

# Nested Unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

# 9 and 15 are used for proper spacing in result. .4f denotes number of decimal
main()
