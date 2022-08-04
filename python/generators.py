#   https://youtu.be/HGOBQPFzWKo?t=12933
#   https://youtu.be/oy5EeamF_M8

#  Generators are funtions thats returns an obj that can be iterated over.
#  They generate the items inside the obj lazily, one at a time & only when you ask for it
#  Thus they are memory efficient when dealing with large data sets


def mygen(input_list):
    for it_em in input_list:
        yield it_em


g = mygen([2,4,6,8,10])
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


g = mygen([2,4,6,8,10])
for x in range(5):
    print(next(g))
