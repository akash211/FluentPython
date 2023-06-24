d = dict(a=10, b=20, c=30)
values = d.values()  # create dict_values object
print(values)
print(type(values))
print(list(values))
print(len(values))

# A view object is a dynamic proxy. If the source dict is updated, you can immediately see the changes through an existing view.
d['z'] = 99
print(d)
print(values)  # we can see the changes in values object
