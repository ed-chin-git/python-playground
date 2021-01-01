#  Tuples :  ordered , immutable,  allows dupes
#  store elements that belong together
#  https://youtu.be/HGOBQPFzWKo?t=991
import utils_edchin.pyxlib as sysx
sysx = sysx()
sysx.clear_terminal()

# DEFINING TUPLES
print('DEFINING TUPLES ............\n')

my_tuple = ('Ed', 32, 'Houston')
print(my_tuple, type(my_tuple))


## THIS IS NOT A TUPLE !!! ( a string)
my_tuple = ('Ed')  # 
print(my_tuple, type(my_tuple))

## THIS IS A Single-element TUPLE 
my_tuple = ('Ed',)  # 
print(my_tuple, type(my_tuple))

## tuple function 
any_iterable = ['Ed', 32, 'Houston']
my_tuple = tuple(any_iterable)
print(my_tuple, type(my_tuple))

# ACCESSING TUPLE ELEMENT ......  
#   zero-indexed
print('\nACCESSING TUPLE ELEMENT ......\n')
ind = 0
tuple_item = my_tuple[ind]
print('Tuple item:', str(ind+1), tuple_item, '\n')

c=0
for my_element in my_tuple:
    c+=1
    print('Tuple item:', str(c),  my_element)
