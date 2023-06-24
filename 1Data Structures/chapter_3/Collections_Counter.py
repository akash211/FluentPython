# A mapping that holds an integer count for each key.
import collections

ct = collections.Counter('gallahad')
print(ct)
ct.update('rodeo')
print(ct)
ct['r'] = -2
print(ct)
print(ct.most_common(2))
print(sum(ct.values()))

list_ct = collections.Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(list_ct)
ct.update(['red', 'green', 'blue', 'violet', 'red', 'violet'])
print(list_ct)
print(list_ct.most_common(2))
print(list_ct["red"])
print(list_ct["rad"])  # It does not throw an error. It returns 0.

