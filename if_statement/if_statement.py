#5-3

alien_colour = "yellow"

if alien_colour == "green" :
    print("You have just earned 5 Points.")
else:
    print("Kill yellow and earn points.")

#5-4

alien_colour = "green"

if alien_colour == "green" :
    print("You have just earned 5 Points.")
else:
    print("You have just earned 10 Points.")

if alien_colour == "yellow" :
    print("You have just earned 5 Points.\n")
else:
    print("You have just earned 10 Points.\n")


#5-5

alien_colour = "green"

if alien_colour == "green":
    print("You have just earned 5 points.")
elif alien_colour == "yellow":
    print("You have just earned 10 points.")
elif alien_colour == "red":
    print("You have just earned 15 points.")

alien_colour = "yellow"
if alien_colour == "green":
    print("You have just earned 5 points.")
elif alien_colour == "yellow":
    print("You have just earned 10 points.")
elif alien_colour == "red":
    print("You have just earned 15 points.")


alien_colour = "red"
if alien_colour == "green":
    print("You have just earned 5 points.")
elif alien_colour == "yellow":
    print("You have just earned 10 points.")
elif alien_colour == "red":
    print("You have just earned 15 points.")


#5-6

age = 100

if age < 2:
    print("The person is a baby.")
elif age == 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65 :
    print("The person is a Adult. ")
else:
    print("The person is elder.")

#5-7

favourite_fruits = ['banana', 'mango' , 'apple' ,'oragne']

fruit = 'grapes'
if fruit == favourite_fruits:
    print("You really like "+ fruit)
else:
    print(fruit + " is not the favourite fruits of yours.")

fruit = 'banana'
if fruit in favourite_fruits:
    print("You really like "+ fruit)
else:
    print(fruit + " is not the favourite fruits of yours.")


#5-8 Hello Admin
print("\n")
users = ['admin' , 'binod' , 'sita' , 'tara' , 'hari']

for user in users:
    if user == 'admin':
        print("Hello Admin would you like to see status report .")
    else:
        print("Hello "+user+", thank you for logging again.")

#5-9 No users

print("\n")

if len(users) == 0 :
    print("We need to find some users ! ")
else:
    print("We have "+str(len(users))+ " users")

#5-10 Checking Usernames

current_users = ['Ram','hari','sita','Tara']

for val in range(len(current_users)):
    current_users[val]=current_users[val].lower()
    print(current_users)

new_users = ['RaM','shyam','gita','tara']

for user in new_users:
    if user.lower() in current_users:
        print("The username "+user+ " has already been taken. ")
    else:
        print(user+ " username is available")

#5-11 Ordinal Number

print("\n")

number = [1,2,3,4,5,6,7,8,9]

for n in number:
    if n in number[:3]:
        print(str(n)+"rd\n")
    elif n in number[3:10]:
        print(str(n)+"th\n")

