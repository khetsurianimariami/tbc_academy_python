from datetime import date
from forex_python.converter import CurrencyRates

year = int(input("Please enter your year: "))
month = int(input("Please enter your  month: "))
number = int(input("Please enter your number : "))
amount_deposited = float(input("Please enter amount of deposit : "))

day_making_deposit = date(year=year, month=month, day=number)
c = CurrencyRates()
full_deposit = amount_deposited * c.get_rate('USD', 'BTC', day_making_deposit)

today = date.today()
my_profit = full_deposit * c.get_rate('BTC', 'USD', today) - amount_deposited

if my_profit > 0:
    print("My profit is ", my_profit)
elif my_profit < 0:
    print("My loss is ", abs(my_profit))
else:
    print("I don't have any profit or loss")







