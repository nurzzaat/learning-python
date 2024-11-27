#1 task
name = 'Nurzat'
print(name)

favoriteQuote = 'No Boundaries in Life' #shortly NBL
print(favoriteQuote)

emptyString = ''
if emptyString == '':
    print('Мұнда ештеңе жоқ')
else:
    print('Ол мен ойлағандай бос емес екен')

#2 task
city = 'Shymkent' 
region = 'South Kazakh Region'
home = city + ', ' + region 
print(home)

introduction = 'Мен осы жерде өмір сүремін: '  
print(introduction + home)

name = 'Nurzat'
age = 20
print(f'My name is {name}, next year I will be {age + 1}')

#3 task
name = 'Baha' 
surname = 'Festival'
fullName = name + ' ' + surname 
print(fullName)

previousBest = 28000
newBest = 35000
congratulations = f"{fullName}, құттықтаймыз! Сіз алдыңғы қадамдар рекордыңызды {previousBest}, кеше {newBest} қадам жасау арқылы жаңарттыңыз!"
print(congratulations)

#4 task
nameInCaps = "NURZAT"
name = "nurzat"
if nameInCaps.lower() == name:
    print('Бұл екі жолдар тең')
else:
    print('Бұл екі жолдар тең емес')  
    
#5 task
name = "Robert Downey Jr."
if 'Jr.' in name:
    print('Бұл атауды екінші буын қолданады')

#6 task
print(len(nameInCaps))

#7 task
text = input("Please enter a text: ")
text = text.replace('bad' , 'good')
print(text)
    
#8 task
string = input("Please enter a string: ")
substring = input("Please enter a substring: ")
index = string.index(substring)
print(index)

#9 task
string = input("Please enter a string: ")
string = string.upper()
print(string)
