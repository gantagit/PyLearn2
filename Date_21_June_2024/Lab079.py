# Ordered Dict

from collections import OrderedDict

d = OrderedDict()
d[1] = 'a'
d['name'] = "Vijay£"
d[2] = 'b'

print(d)

for  k,v in d.items():
    print(k,v)
