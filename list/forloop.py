#4-1

pizzas = ['chicken' , 'sausage' , 'mushroom']

for pizza in pizzas:
    print("I want to order  "+pizza.title() +" pizza.")
    print("Cause I love it.\n")
print('We will have your order soon please wait.')

#4-3


for numb in range(1,21):
    print(numb)


#4-5

stat = []
for num in range(1,1000001):
    eg = num
    stat.append(eg)
print(sum(stat))
print(min(stat))
print(max(stat))
print("\n")
#4-6

for odd in range(1,21,2):
    print(str(odd))
    print("\n")

#4-7

for mul in range(1,11):
    val = 3 * mul
    print(str(val))
    print("\n")


#4-8

cubes = []
for cube in range(1,11):
    cube = cube**3
    cubes.append(cube)
print(cubes)
print("\n")
#4-9

cubes = [cube**3 for cube in range(1,11)]
print(cubes)

print("\n")

#4-10

print("The 3 elements of the list are : ")
for slice in cubes[0:3]:
    print(slice)
a = len(cubes)
print("The lenght of cubes is: "+str(a))
print("The middle elemetns of the lists are : ")
for slice in cubes[4:8]:
    print(slice)

print("Last 3 items are : ")
for slice in cubes[-3:]:
    print(slice)

print("\n")
#4-11

#pizzas = ['chicken' , 'sausage' , 'mushroom']

friend_pizza = pizzas[:]
print(pizzas)
print(friend_pizza)

pizzas.append("Buff")
friend_pizza.append("cheese")

print("My fav pizza are : ")
for piz in pizzas[ : ]:
    print(piz)
print("My friend fav pizza are : ")
for pizza in friend_pizza[ : ]:
        print(pizza)

#4-13
print("\n")
food = ('momo','chowemein','chana','pasta','boiled_egg')
for item in food:
    print(item)
print("\n")
food = ('momo','chowemein','chana','fried_rice','french_fry')
for item in food:
    print(item)

