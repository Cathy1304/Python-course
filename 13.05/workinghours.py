import sys

hours = int(input())
day = input()

if hours >= 10 and hours <= 18:
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thurdsay" or day == "Friday" or day == "Saturday":
        print("open")
    elif day == "Sunday":
        print("closed")
    else:
        print("closed")
else:
    print("closed")