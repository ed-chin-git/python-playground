import utils_edchin.pyxlib as pyx 
pyx = pyx()
pyx.clear_terminal()


# STRINGS
# Based on https://youtu.be/HGOBQPFzWKo

print('\nSTRINGS.........')

x = ['a', 'p', 'p', 'h', 's']


search_for = 'p'
print('list = ', x)
print( search_for, 'occurs', x.count(search_for), 'times.')