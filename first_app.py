# Write your code here
Bubblegum = 202
Toffee = 118
Ice_cream = 2250
Milk_chocolate = 1680
Doughnut = 1075
Pancake = 80
Income = Bubblegum + Toffee + Ice_cream + Milk_chocolate + Doughnut + Pancake

print('Earned amount:')
print('Bubblegum: $202')
print('Toffee: $118')
print('Ice cream: $2250')
print('Milk chocolate: $1680')
print('Doughnut: $1075')
print('Pancake: $80')
print('Income: $', Income)
staff_expense = input("Staff expenses:")
print("Staff expenses:", staff_expense)
other_expense = input("Other expenses:")
print("Other expenses", other_expense)
float1 = float(Income)
float2 = float(staff_expense)
float3 = float(other_expense)
net_income = float1 - float2 - float3
print("Net income: $", net_income)