date_time = input("Please enter time like this: year-month-dayThour:minute:second.mstimezone:  ")

print("Input: ", date_time)

plus_minus = "-, +"

date = ""

time = ""

time_zone = ""

i = 0
while date_time[i] != "T":
    date = date + date_time[i]
    i += 1

j = date_time.index("T") + 1
while date_time[j] not in plus_minus:
    time = time + date_time[j]
    j += 1

if "+" in date_time:
    k = date_time.index("+")
    while k < len(date_time):
        time_zone = time_zone + date_time[k]
        k += 1
else:
    k = date_time.index("-")
    while k < len(date_time):
        time_zone = time_zone + date_time[k]
        k += 1

print("Output:", date[8:10] + date[4:7] + "-" + date[0:4], end=" ")

if int(time[0:2]) > 12:
    print(str(int(time[0:2]) - 12) + time[2:6] + str(int(float(time[6:len(time)]))), end=" ")
else:
    print(time[0:2] + time[2:6] + str(int(float(time[6:len(time)]))), end=" ")

print(time_zone[0] + time_zone[2])
