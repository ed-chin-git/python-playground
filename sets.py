# SET data structure : unordered, mutable, no dupes
# Based on https://youtu.be/HGOBQPFzWKo?t=2561
import utils_edchin.pyxlib as pyx
pyx = pyx()
pyx.clear_terminal()

print('Creating SETS.....')

# empty sets
set_0 = set()  #  cannot use {}

# using curly braces
set_1 = {3, 5, 7, 32, 7,  77, 2, 22}   

# using the set() function
lis_t = [3, 5, 9, 9, 9, 7, 7, 7, 12, 55, 33, 1]
set_2 = set(lis_t)

print('\nset_0:', set_0)
print('set_1:', set_1)
print('set_2:', set_2)

print('\nAdd elements.....')
set_1.add(147)
set_1.add(454)
set_1.add(838)
print('set_1:', set_1)

print('\nRemove elements.....')
set_1.remove(77) # will throw key error if non-existant
set_1.remove(22)
#    OR
set_1.discard(11) # will not throw key errors
set_1.discard(11)
set_1.discard(5)

print('set_1:', set_1)


print('\nRemove all elements.....')
set_1.clear()
print('set_1:', set_1)




