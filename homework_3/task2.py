from datetime import date
import calendar

day_names = list(calendar.day_name)

birth_year = int(input("Please enter your birth year: "))
birth_month = int(input("Please enter your birth month: "))
birth_number = int(input("Please enter your birth number : "))

birthday_of_week = date(birth_year, birth_month, birth_number).weekday()
print(f"You You were born on {day_names[birthday_of_week]}")




