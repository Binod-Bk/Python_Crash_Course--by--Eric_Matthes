# 3-1
friends = ["sanaya" , "pramod", "shijal" , "saurabh" ]
print(friends[0].upper(),friends[1].lower(),friends[2].title(),friends[3])

#3-2

message = "Good Morning "
print(message+"\n"+friends[0]+"\n"+friends[1],friends[2],friends[3])
print("\n")
#3-3
vehicle = ["pulsar","dirt"]
print("I Would like to own a "+vehicle[0]+" or "+vehicle[1])

#3-4
guest = ["ram","tara","khaisara","sita","binita"]
message = "Please come to my Birthday Party "
print(message+guest[0])
print(message+guest[1])
print(message+guest[2])
print(message+guest[3])
print(message+guest[4])

#3-5
print("\n")
no_guest = "sita"
guest[3]= "harikala"
print(message+guest[0])
print(message+guest[1])
print(message+guest[2])
print(message+guest[3])
print(message+guest[4])

#3-6
guest.insert(0,"binod")

guest.insert(4,"jackson")

guest.append("rajesh")
print("\n")
print(message+guest[0])
print(message+guest[1])
print(message+guest[2])
print(message+guest[3])
print(message+guest[4])
print(message+guest[5])
print(message+guest[6])
print(message+guest[7])

print("\n Only two guest can be invited\n")

pop_item=guest.pop();
print("Sorry "+pop_item+" you are not invited.")

pop_item=guest.pop();
print("Sorry "+pop_item+" you are not invited.")
pop_item=guest.pop();
print("Sorry "+pop_item+" you are not invited.")
pop_item=guest.pop();
print("Sorry "+pop_item+" you are not invited.")
pop_item=guest.pop();
print("Sorry "+pop_item+" you are not invited.")
pop_item=guest.pop(0);
print("Sorry "+pop_item+" you are not invited.")

print(guest[0],guest[1])

print("You are still invited "+guest[0])
print("You are still invited "+guest[1])

del guest[1]
del guest[0]
print(guest)
print("Hello World")



#3-8

print('\n\n\n')

places = ['paris' , 'everest', 'mustang' , 'america']
print("The places I would like to visit are:")
print(places)

print(sorted(places))
print(places)
print(sorted(places , reverse=True))

print(places)
places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)


print('\n\n\n')

#3-9

print("The length of the guest list is :" + str(len(guest)))


#3-10
print('\n\n\n')
mylist = ['sagarmatha' , 'tesla' , 'python' ,'java' , 'rajesh_hamal' ,  'roses']
print(mylist)
mylist.append('binita')
print(mylist)
mylist.insert(4, 'tara')
print(mylist)
del mylist[1]
print(mylist)

mylist.pop()
print(mylist)
mylist.pop(0)
print(mylist)
rm = mylist.pop(4)
print(mylist)
print(rm)
mylist.remove('java')
print(mylist)
mylist.append('binod')
mylist.insert(2,'puran')
print(mylist)
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
print(sorted(mylist))
print(sorted(mylist , reverse=True))
mylist.append('ram')
print(mylist)
mylist.reverse()
print(mylist)
print("The length of mylist lists is :" + str(len(mylist)))




