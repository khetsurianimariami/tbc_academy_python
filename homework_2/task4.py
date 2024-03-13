car_speed = float(input("Please enter car speed in km/h: "))

if car_speed <= 30:
    print("Category of car is SLOW")

elif (car_speed > 30) and (car_speed <= 60):
    print("Category of car is MODERATE")

elif (car_speed > 60) and (car_speed <= 120):
    print("Category of car is FAST")

else:
    print("Category of car is VERY FAST")


