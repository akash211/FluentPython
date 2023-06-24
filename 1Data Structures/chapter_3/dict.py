def dump(**kwargs):
    return kwargs


print(dump(**{'x': 1}, y=2, **{'z': 3}))

print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})  # previous x got overwrited

# | created new mapping
d1 = {'a': 0, 'x': 1, 'y': 2}
d2 = {'z': 3, 'x': 4}
print(d1 | d2)
print(d1)

d1 |= d2
print(d1)
print(d2)


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')


b1 = dict(api=1, author='Douglas Hofstadter',
          type='book', title='Gödel, Escher, Bach')
print(get_creators(b1))
from collections import OrderedDict

b2 = OrderedDict(api=2, type='book',  # even if Dict is not ordered, it is still ordered
                 title='Python in a Nutshell',
                 authors='Martelli Ravenscroft Holden'.split())
print(get_creators(b2))

# print(get_creators({'type': 'book', 'pages': 770}))   # ValueError
# print(get_creators('Spam, spam, spam'))  # ValueError

food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:  # ** can be used as last paramater.
        print(f'Ice cream details: {details}')
