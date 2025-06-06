result = 0
def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(4))
print(adder(5))

result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

def adder2(num):
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self,num):
        self.result +=num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

class Service:
    secret = "지구는 4006년에 멸망한다."
an = Service()
print(an.secret)
Service.secret = "지구는 4006년에 멸망한다는 사실을 뻥이다."
print(an.secret)

class Service:
    secret = "지구는 4006년에 멸망한다."
    def sum(self,a,b):
        result = a+b
        print("%s+%s = %s이다." %(a,b,result))

an = Service()
an.sum(1,1)

class Service:
    secret = "지구는 4006년에 멸망한다."
    def setname(self,name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님, %s+%s = %s이다." % (self.name, a, b, result))

an = Service()
an.setname ("박달도사")
an.sum(1,1)

kim = Service()
park = Service()
kim.name = "김정보"
park.name = "박융합"
print(kim.name)
print(park.name)
kim.secret = "비밀은없다"
print(park.secret)
print(kim.secret)
print(Service.secret)


class Service:
    secret = "지구는 4006년에 멸망한다."
    def __init__(self,name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님, %s+%s = %s이다." % (self.name, a, b, result))
an = Service("박달도사")
an.sum(1,1)

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4, 2)
print(a.sum())

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,7)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
print(b.sub())

import random

player1_dice = []
player2_dice = []

for i in range(3):
    player1_dice.append(random.randint(1,6))
    player2_dice.append(random.randint(1,6))

print("Player 1 rolled" + str(player1_dice))
print("Player 2 rolled" + str(player2_dice))

if sum(player1_dice) == sum(player2_dice):
    print("Draw")
elif sum(player1_dice) > sum(player2_dice):
    print("Player 1 wins")
else :
    print("Player 2 wins")

from random import randint

class Player:
    def __init__(self):
        self.dice=[]
    def roll(self):
        self.dice =[]
        for i in range(3):
            self.dice.append(randint(1,6))
    def get_dice(self):
        return self.dice

player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

print("Player 1 rolled" + str(player1.get_dice()))
print("Player 2 rolled" + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()):
    print("Draw")
elif sum(player1.get_dice()) > sum(player2.get_dice()):
    print("Player 1 wins")
else :
    print("Player 2 wins")

class Customer(object):

    def __init__(self, name):
        self.name = name
    def set_balance(self,balance = 0.0):
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance