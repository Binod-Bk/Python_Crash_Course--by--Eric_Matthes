


# 7-1 Rental Car

# car = input("Seller : What kind of Rental Car would you like to see ? \n Customer : ")
# print("Seller : Let me see if I can find you a "+car)

#7-2 Resturant Seating

# rest = input("How many people will there be in dinner table ?  ")
# rest  = int(rest)
#
# if rest>8:
#     print("You will have to wait for the table . ")
# else:
#     print("Your table is ready sir . ")

#7-3 Multiples of ten

# numb = input("Enter a number to see if it is divisible by 10 or not . ")
# num = int(numb)
# if num%10 == 0:
#     print("The number "+str(num)+ " is divisible by 10 .")
# else:
#     print("The number "+str(num)+" is not divisible by 10 .")

#7-4 Pizza Toppings

# pizzas=[]
# active = True
# while active:
#
#     pizza = input("What topping would you like to have ? \n Press 'quit' to exit . ")
#     if pizza == "quit":
#         active = False
#     else:
#         pizzas.append(pizza)
#         print("We will have your pizza ready with ")
#         for pizz in pizzas:
#             print(pizz)
#         print("toppings .")


# 7-5 Movie Tickets

# while True:
#         user = input("What is your age ? ")
#         user = int(user)
#         if user <= 3:
#              print("The cost of your ticket is free .")
#
#         elif user>3 and user<12:
#              print("The cost of your ticket is $10 .")
#
#         else:
#             print("The cost of your ticket is $15 .")


#7-6 Three Exists

#conditional test

# pizzas=[]
#
# piz= " "
# while piz!= "quit":
#     piz = input("What toppings would you like to have in your pizza ? ")
#     pizzas.append(piz)
#     if piz != 'quit':
#         print("Your pizza with the following toppings will be ready . ")
#         print("List of toppings are : ")
#         for pizza in pizzas:
#             print(pizza)

#break

# pizzas=[]
#
# piz= " "
# while True:
#     piz = input("What toppings would you like to have in your pizza ? ")
#     if piz == 'quit':
#         break
#     else:
#         pizzas.append(piz)
# print("Your pizza with the following toppings will be ready . ")
# print("List of toppings are : ")
# for pizza in pizzas:
#     print(pizza)

#activate variable

# pizzas=[]
# active = True
# while active:
#
#     pizza = input("What topping would you like to have ? \n Press 'quit' to exit . ")
#     if pizza == "quit":
#         active = False
#     else:
#         pizzas.append(pizza)
#         print("We will have your pizza ready with ")
#         for pizz in pizzas:
#             print(pizz)
#         print("toppings .")


#7-7 Infinity

# a = 0
# while True:
#
#     print(a)
#     a = a + 1

#7-8 Deli

# sandwich_order = ['chicken','buff','cheese','veg']
# finished_sandwich = [ ]
# while sandwich_order:
#     sandwich = sandwich_order.pop()
#     finished_sandwich.append(sandwich)
#     print("I made your "+sandwich+" sandwich.")
# print("List of made sandwiches are : ")
# for sand in finished_sandwich:
#     print(sand)

#7-9 No Pastrami

# sandwich_order = ['pastrami','chicken','buff','cheese','veg','pastrami','pastrami']
# finished_sandwich = [ ]
# print("Deli has run out of Pastrami")
# while 'pastrami' in sandwich_order:
#         sandwich_order.remove('pastrami')
# while sandwich_order:
#     deli = sandwich_order.pop()
#     finished_sandwich.append(deli)
# print("Other finished sandwiches are :")
# print(finished_sandwich)

#7-10 Dream Vacation
# dict = { }
# active = True
# while active:
#     name = input("What is your name?")
#     places = input("Where do you want to go for Vacation ? ")
#     dict[name]=places
#     repeat = input("Would you still like to continue polling ? (yes/no) .")
#     if repeat == 'no':
#         active = False
# print("The result of poll is :")
# for key,value in dict.items():
#     print(key+" would like to go "+value+" for the vacation.")




