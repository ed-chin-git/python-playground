# Based on https://youtu.be/HGOBQPFzWKo?t=1790

# DICTIONARY data structure : Key-Value pairs, unordered, mutable

import utils_edchin.pyxlib
pyx = utils_edchin.pyxlib()
pyx.clear_terminal()

campN={}
campN[(1,3,5)]=2
campN[(3,2,1)]=6
campN[(1,3)]=10

sum=0
for k in campN:
    sum += campN[k]

# print(len(campN)+sum)

for i in campN:
    print(i)

