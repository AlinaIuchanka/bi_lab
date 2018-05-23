# Write a program to calculate total cost. One item costs M dollars and N cents
# Customer bought L items. Print total price in dollars and cents for L items
import re

str_input = input("Input dollars, cents, items count:\n")
list_input = list(map(int, filter(None, re.split("\D+", str_input))))
total_cents = list_input[1]*list_input[2] % 100
total_dollars = list_input[0]*list_input[2] + list_input[1]*list_input[2] // 100
print(("Total cost: {dollars} dollars {cents} cents".
       format(dollars=total_dollars, cents=total_cents)))
