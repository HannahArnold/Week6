import random
# First block
for i in range(10):
    print(i)
# Second desk
print(‘hello’)
#  extra
print(len(‘hello’))
print(‘hello’[2])
# print( random.randint(1,10) )
# Length of below string is 15
string = “geeks for      geeks”
print(len(string))
print random.randint(1,101)
string = ‘GeeksforGeeks’
print(string.isupper())
string = ‘My name is ayush’
print(string.upper())
print(‘hello’.upper())
print(‘All around the world’[7].upper())
name = ‘Mark’
age = 30
like_soup = False
print(name)
print(name, age, like_soup)
i = 10
i = i + 2
print(i)
favourite_drink = “wine”
print(‘My favourite drink is {}’.format(favourite_drink))
music = ‘sams music’
if music == “sams music”:
    print(“oh no it’s 00s indie again”)
elif music == “No music”:
    print(“Peace and quiet”)
else:
            print(‘What music is playing?’)
place =‘Cambles’
weather = ‘Rain’
if place == “Cambles” and weather == ‘Sunny’:
    print(“Check”)
elif place == “Cambles” and weather == ‘Rain’:
    print(“Obvs”)
else:
            print(‘what it isnt sunny’)
# def press_grind_beans():
#      print(‘Grinding for 20 seconds’)
# press_grind_beans()
#
coffee_is_grinding = False
def press_grind_beans():
    if coffee_is_grinding:
        print(‘The coffee is grinding’)
    else:
        print(‘The coffee is not grinding’)
press_grind_beans()
##############
def cash_withdrawal(amount,accnum):
    print(“Withdrawing {} from account {}“.format(amount,accnum))
cash_withdrawal(300, 50449921)
cash_withdrawal(10, 50449921)
cash_withdrawal(5, 50449921)
def multiply(num1,num2):
    return num1 * num2
print(multiply(2,3))
coffee_order = [
    ‘Sam - Hot Chocolate’,
    ‘Andrew -Flat White’,
    ‘Ezra - Champagne’
]
print(coffee_order)
print(coffee_order[2])
print(len(coffee_order))
coffee_order.append(‘Stuart - Champers’)
print(coffee_order)
coffee_order.reverse()
print(coffee_order)