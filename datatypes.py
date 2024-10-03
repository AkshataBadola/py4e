#Tuples

# this is packing of variables in a tuple
tuple1 = (1,2,3)
print(tuple1[1])
print(tuple1[1:3])

tuple2 = ([1,2], [3,4])
print(tuple2[0])
print(tuple2[0][1])

#unpacking
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
(green, *tropic, red) = fruits
print(green)
print(yellow)
print(tropic)
print(red)

#multple return statements
def simple_function():
    return 0, 1

print(simple_function())


#defining
d1 = {}
d1[1] = "one"
d1[2] = "two"
print(d1)

d2 = {1 : 'one', 'hello': True}
print(d2)
print(d1[1])
print(d1.keys())
print(d1.items())
print(d1.values())

d = {1: 'one', 2: 'two', 3: 'three'}
for key, value in  d.items():
    print(key, value)


#sets
s = ['apple', 'orange', 'banana', 'kiwi']
fruit = set(s)
print(fruit)
print('apple' in s)
print('guava' in s)
print('Akshata' in s)
