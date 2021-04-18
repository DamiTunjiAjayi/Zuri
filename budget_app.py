
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(10000, "initial deposit")
food.withdraw(2000.35, "groceries")
food.withdraw(1500.50, "eatery and more food for friends")
print(food.get_balance())


clothing = budget.Category("Clothing")
food.transfer(1000, clothing)
clothing.withdraw(500.25)
clothing.withdraw(400.75)


entertainment = budget.Category("Entertainment")
food.transfer(1500, entertainment)
entertainment.deposit(3500, "initial deposit")
entertainment.withdraw(2000)

print(food)
print(clothing)
print(entertainment)

print(create_spend_chart([food, clothing, entertainment]))