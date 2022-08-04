# ______________  COLLECTIONS 
# Data structures : Counter, namedtuple, OrderedDict,  defaultdict, deque
# Based on https://youtu.be/HGOBQPFzWKo?t=4970

import utils_edchin.pyxlib as pyx 
pyx = pyx()
pyx.clear_terminal() 

# __________________  COUNTER _________________________
# container that stores the elements as dictionary keys
# and their count as values
from collections import Counter 
list_1 = ["bill", "ed", "sam", "bill", "ted", "sam", "sam", "sam"]

countr_1 = Counter(list_1)

print('List :', list_1)
print(countr_1)
print(countr_1.items())
print(countr_1.keys())
print(countr_1.values())

print('.most_ common', countr_1.most_common(1))
print('.most_ common[key]', countr_1.most_common(1)[0][0])
print('.most_ common[value]', countr_1.most_common(1)[0][1])
print('.element returns an iterable:', countr_1.elements())
print(list(countr_1.elements()))


# ________________ NAMED TUPLE _______________
from collections import namedtuple


from collections import OrderedDict
from collections import defaultdict
from collections import deque
