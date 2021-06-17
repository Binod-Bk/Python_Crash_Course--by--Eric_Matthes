#6-1 Person

persons = { "first_name":"tara","last_name":"bk","age":"38","city":"kathmandu"}

print(persons)
for person in persons.items():
    print(person)

#6-2 Favourite Number
print("\n")
people = {"binod":8,"tara":10,"ram":20,"binita":7}

for key,value in people.items():
    print("The favourite number of "+key+ " is "+str(value))


#6-3 Glossary and 6-4

print("\n")

glossary = {"condition": "any situation", "lists": "collection of related data",
            "dictionary": "defines the nature of data", "variable": "something that contains the information",
            'compiler': "program that check the code"}
glossary['statement']="something that is written"
print(glossary)
for key,value in glossary.items():
    print(key+" : "+value+"\n")


#6-5 Rivers

rivers = { "nile":"egypt","karnali":"Nepal","nigra fall":"South Africa","ganga":"india"}


for river,counrty in rivers.items():
    print("The "+river+" runs through "+counrty)

print("\nThe list of rivers are : ")
for river in rivers.keys():
    print(river)

print("\nThe list of countries are : ")
for country in rivers.values():
    print(country)
print('\n')

#6-6 Polling

poll_people = ['jen', 'sarah','edward','phil','binod','tara','sita']

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for key in poll_people:
    if key not in favorite_languages.keys():
        print("Hello Dear "+key+", we invite you to take a poll. ")
    elif key in poll_people:
        print("Dear "+key+", thank you for responding in our poll.")


#6-7 People
print('\n')
persons1 = { "first_name":"tara","last_name":"bk","age":"38","city":"Parbat"}
persons2 = { "first_name":"binod","last_name":"bk","age":"22","city":"Parbat"}
persons3 = { "first_name":"binita","last_name":"bk","age":"20","city":"kathmandu"}
persons4 = { "first_name":"ram","last_name":"bk","age":"45","city":"Syangja"}

peoples = [persons1,persons2,persons3,persons4]

print(peoples)
print('\n')

for people in peoples:
    print(people)
    print("\n")


#6-8 pets

fucche = { 'kind':'dog','owner':'tara'}
fucchi = { 'kind':'dog','owner':'tara'}
cherry = { 'kind':'cat' , 'owner':'sanaya'}
doraemon = {'kind':'robot','owner':'nobita'}

pets = [fucche,fucchi,cherry,doraemon]

for pet in pets:
    print(pet)

#6-9 Favourite places

#6-10 Favourite Numbers


# print("\n")
# people = {"binod":8,"tara":10,"ram":20,"binita":7}
#
# for key,value in people.items():
#     print("The favourite number of "+key+ " is "+str(value))


print("\n")
bin = [8,7,5]
tar = [10]
ra = [5,7,3]
bini = [4,8,100]

people = {"binod":bin,"tara":tar,"ram":ra,"binita":bini}

for key,value in people.items():
    print("The favourite number of "+key )
    for val in value:
        print(val)

#6-11 Cities

ktm = { 'country':'nepal','population':20520450,'fact':'city of temples'}
pokhara = {'country':'nepal', 'population':2055656, 'fact':'rains most of the time'}
mustang = { 'country':'nepal', 'population':42556, 'fact':'has a burning flame temple muktinath'}

cities = {'ktm':ktm,'pokhara':pokhara,'mustang':mustang}

print('\n')
for key,value in cities.items():
    print("City : "+key)
    for key2,val in value.items():
        print(key2+" = \t"+str(val))


#6-12









