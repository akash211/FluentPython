x = 'ABC'

codes = [ord(x) for x in x]
print(x)  # x did not mess up
print(codes)

walrus_codes = [last := ord(c) for c in x]
print(last)
print(walrus_codes)
# print(c)  # c existed only inside the listcomp

symbols = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)


colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts1 = [(color, size) for size in sizes for color in colors]

# both are different in order
print(tshirts)
print(tshirts1)
