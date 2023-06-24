# Python dictionaries are ordered in Python 3.6 and later. However, there are still some differences between OrderedDict and dict.
# OrderedDict preserves the order in which the keys were inserted.
# A regular dict doesn't track the insertion order, and iterating it gives the values in an arbitrary order.
# By contrast, the order the items are inserted is remembered by OrderedDict.
# The order of the keys in a dictionary is not guaranteed to be consistent across different runs of the program, or even across different calls to the same function.
# This is because the order of the keys is maintained by a hash table, and the hash table may be re-hashed if it becomes too full.
# OrderedDict has a few extra methods. For example, OrderedDict has a move_to_end() method that allows you to move an item to the end of the dictionary.
# OrderedDict is slightly slower than dict. This is because OrderedDict has to keep track of the order of the keys, which takes up some extra memory and processing time.
