"""Build an index mapping word -> list of occurrences"""

import collections
import re
import sys

index = collections.defaultdict(list)

index['language'] = ['Python', 'Ruby']
index['database'] = ['sql server', 'Redshift']
index['framework'] = ['Django', 'Rails']

print(index)

print(index['language'])
print(index['something'])  # No error but a list is now added for this keyword in dictionary
print(index)
# The default_factory of a defaultdict is only invoked to provide default values for __getitem__ calls, and not for the other methods.
# For example, if dd is a defaultdict, and k is a missing key, dd[k] will call the default_factory to create a default value,
# but dd.get(k) still returns None, and k in dd is False.
