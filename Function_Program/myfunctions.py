

#8-1 Message

def display_message():
    print("What are you learning in this Chapter ? ")

display_message()
print("\n")
#8-2 Favourite Books

def favourite_book(title):
    print("One of my favourite Book is "+title)

favourite_book("Python Crash Course")
print("\n")
#8-3 T-Shirts

# def make_shirt(size,message):
#     print("I want to make a t-shirt of size "+size+" with message '"+message+"' .")
#
# mymessage = "Chill and Rock On"
# make_shirt('large',mymessage)
# make_shirt(size='medium',message='Hello is My Message ')

#8-4 Large Shirts

# def make_shirt(message,size='Large'):
#     print("I want to make a t-shirt of "+size+" size with message '"+message+"' .")
#
# make_shirt('I love Python')

def make_shirt(size,message='This is My Message'):
    print("I want to make a t-shirt of "+size+" size with message '"+message+"' .")

make_shirt('Medium')
make_shirt('Large')
print("\n")

#8-5 Cities

def descibe_city(city,country="Nepal"):
    print(city+" is in "+country)

descibe_city('Kathmandu')
descibe_city('Pokhara')
descibe_city('New York')
print("\n")

#8-6 City Names

def city_contry(city,country):
    formatted_string = '"'+city+", "+country+'"'
    return  formatted_string

a = city_contry('Kathmandu','Nepal')
print(a)
b = city_contry('New York','USA')
print(b)
print(city_contry('Wuhan','China'))

print("\n")


#8-7 Album

# def make_album(artist,album,tracks=''):
#
#     if tracks:
#         dict = {'artist':artist,'album':album,'tracks':tracks}
#     else:
#         dict = {'artist':artist,'album':album}
#     return dict
#
# a = make_album('Michael Jackson','Dangerous','13')
# print(a)
# print(make_album('The Weeknd','After Hours'))
#
# print("\n")
# #8-8 User Album
#
# active = True
# while active:
#     artist = input("What is the Name of the Artist ? \n Enter 'q' to exit. ")
#     album = input("What is the Name of the Album ? \n Enter 'q' to exit. ")
#     if artist=='q' or album=='q':
#         active = False
#     else:
#         dict1={}
#         info = make_album(artist,album)
#         for a, i in info.items():
#             print(a + " " + i)
#
# print("\n")

#8-9 Magicians
#
# magicians = ['binod','sita','hari']
#
# def show_magicians(list):
#     print("The list of magicians are:")
#     for i in list:
#         print(i)
# show_magicians(magicians)
# print("\n")

# #8-10 Great Magicians
#
# magicians = ['binod','sita','hari']
#
# def show_magicians(see):
#     print(see)
#
#
# def make_great(name):
#     modified_name = 'The Great '+name.title()
#     show_magicians(modified_name)
#
#
# def show_magic(list):
#     print("The list of magicians are:")
#     for i in list:
#         make_great(i)
#
# show_magic(magicians)
#
# print("\n")

#8-11 Unchanged Magicians
# magicians = ['binod','sita','hari']
# copy_magicians =magicians[:]
#
#
# def show_magicians(see):
#     print("The unmodified List Names are :")
#     for i in see:
#         print(i)
#
#
# def make_great(name):
#     print("The modified List Names are :")
#     for ii in name:
#         modified_name = 'The Great '+ii.title()
#         print(modified_name)
#
#
# make_great(copy_magicians)
# show_magicians(magicians)
# print("\n")


#8-12 Sandwiches

def sandwiches(*items):
    print("The list of Sandwiches are :")
    for i in items:
        print(i)

sandwiches('chicken')
sandwiches('veg','buff','egg')
sandwiches('chicken','buff','eggs','veg')
print("\n")


#8-13 User Profile

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = { }
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Binod', 'B.K.',
location='Gongabu',
field='BCA',
phone='9808080800')
print(user_profile)
print("\n")


#8-14 Cars

def make_car(brand,model,**items):

    items['Car Brand']=brand
    items['Model']=model
    for x,y in items.items():
        items[x]=y
    return items
a = make_car('Tesla','S1',color='blue',battery='70 KWH')
print(a)
print("\n")

#8-15 Printing Models

import printing_functions

printing_functions.print_model('Tesla S1')
print("\n")


#8-16 Imports
from printing_functions import *
from printing_functions import print_model2 as pm


print_model('Tesla S1')
pm('Tesla S21')
print("\n")

#8-17 Styling








