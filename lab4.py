#1 task
9 == 9
print(True)
print(9 == 9)

9 != 9
print(False)
print(9 != 9)

47 > 90
print(False)
print(47 > 90)

47 < 90
print(True)
print(47 < 90)

4 <= 4
print(True)
print(4 <= 4)

4 >= 5
print(False)
print(4 >= 5)

(47 > 90) or (47 < 90)
print(True)
print((47 > 90) or (47 < 90))

(47 > 90) and (47 < 90)
print(False)
print((47 > 90) and (47 < 90))

not True
print(False)
print(not True)

#2 task
tenge = 0 
if tenge == 0:
    print('Кешіріңіз, бірақ сізде қаражат жеткіліксіз!')

tenge = 300
if tenge == 0:
    print('Кешіріңіз, бірақ сізде қаражат жеткіліксіз!')
elif tenge > 0:
    print('Уау, сізде бәліштерге ақша бар!')

tenge = 2000
if tenge == 0:
    print('Кешіріңіз, бірақ сізде қаражат жеткіліксіз!')
elif tenge < 400:
    print('Уау, сізде бәліштерге ақша бар!')
else:
    print('Біз таксиге отырамыз!')
    
#3 task
hasFish = True
hasPizza = False
hasVegan = False

if (hasPizza or hasFish) and hasVegan:
    print('Кеттік!')
else:
    print('Кешіріңіз, біз басқа орынды таңдауымыз керек')

#4 task
isRainy = False
degree = 29
if degree > 27 or not isRainy:
    print('Мен серуендеймін!')
    
#5 task
season = int(input('Маусым санын енгізіңіз: '))
if season == 1:
    print("Қыс")
elif season == 3:
    print("Жаз")
elif season == 2:
    print("Көктем")
elif season == 4:    
    print("Күз")
    
#6 task
age = int(input('Жасыңызды енгізіңіз: '))
if age > 0 and age <= 2:
    print("Нәресте")
elif age > 2 and age <= 14:
    print("Балалар билеті")
elif age > 14:
    print("Ересектер билеті")

#7 task
price1 = 1000 #dollar
price2 = 2000
expensivePrice = price1 if price1 > price2 else price2
print(expensivePrice)

#8 task
number = int(input('Enter a number: '))
if number % 2 == 0:
    print('The number is even', number)
else:
    print('The number is odd', number)
    
#9 task
age = int(input('Жасыңызды енгізіңіз: '))
isAllowed = True if age >= 18 else False
print(isAllowed)

#10 task
number = int(input('Санды енгізіңіз: '))
if number >= 10 and number <= 20:
    print('The number is located between 10 and 20')


#11 task
cost = int(input('Сомманы енгізіңіз: '))
if cost >= 1000:
    cost -= cost / 10
print(cost)

#12 task
number = int(input('Санды енгізіңіз: '))
if number > 0:
    print('+')
else:
    print('-')
