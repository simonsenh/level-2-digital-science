# importing the required module

import matplotlib.pyplot as plt

name = input("what is your name?")
savings = float(input("How much money do you have?"))
month_income = float(input("How much money do you make a month?"))
month_expense = float(input("How much money do you spend a month?"))
time = float(input("How long do you want to process your finances?"))
loan = float(input("How much is the loan you have borrowed?"))
loan_due = float(input("How long do you want to take to pay of your loan?"))
month_gross = month_income - month_expense

# x axis values
x = [0, loan_due, time]
# corresponding y axis values
y = [savings, (savings - loan) + (month_gross * loan_due), (time * month_gross - loan + savings)]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Months')

# naming the y axis
plt.ylabel('NZ dollars')

# giving a title to my graph
plt.title('{} financial future for the next {} months'.format(name, time))

# function to show the plot
plt.show()
print("yes")
