number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)

number_list = []
for number in range(1,6):
    number_list.append(number)

number_list = list(range(1,6))

number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number-1 for number in range(1,6)]
print(number_list)

a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)

a_list = []
for number in range(1,6):
    if number%2 == 1:
        a_list.append(number)
print(a_list)

sentence = ['I', 'Love', 'Python', 'Soooooo', 'MUCH!!!']

[word.lower() for word in sentence]
print([word.lower() for word in sentence]) # 각 단어를 소문자로 바꾼 결과

[word for word in sentence if len(word) > 6]
print([word for word in sentence if len(word) > 6]) # 문자열 길이가 6 이상인 단어만 고른 결과

[(x, x ** 2, x ** 3) for x in range(10)]
print([(x, x ** 2, x ** 3) for x in range(10)]) #0부터 9까지 각각 x, x², x³를 튜플로 만든 결과

rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

[(i,j) for i in range(5) for j in range(i)]
print([(i,j) for i in range(5) for j in range(i)])

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}

a_set = {number for number in range(1,6) if number % 3 == 1}

def sum(a,b):
    return a+b

print(sum(1,2))
print(sum(1.3,3.1))
print(sum('love ','python'))

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
list( zip(english, french) )
# [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]
dict( zip(english, french) )
# {'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken', 'cake')
{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}

menu(entree='beef', dessert='bagel', wine='bordeaux')
{'dessert': 'bagel', 'wine': 'bordeaux', 'entree': 'beef'}

menu('frontenac', dessert='flan', entree='fish')
{'entree': 'fish', 'dessert': 'flan', 'wine': 'frontenac'}

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken')
{'dessert': 'pudding', 'wine': 'chardonnay', 'entree': 'chicken'}

menu('dunkelfelder', 'duck', 'doughnut')
{'dessert': 'doughnut', 'wine': 'dunkelfelder', 'entree': 'duck'}

def menu(price, wine='chardonnay', entree='chicken’, dessert=‘pudding'):
    return {'price': price, 'wine': wine, 'entree': entree, 'dessert': dessert}

menu(100)
menu(price=100)
menu(price=120, entree='beef')
##menu(dessert='bagel', price=110)
menu('eighty' 'saint-pierre', 'fish')
##menu('hundred' wine='saint-pierre')

def echo(anything):
    return anything

help(echo)