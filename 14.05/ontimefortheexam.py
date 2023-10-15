import sys

examHour = int(input())
examMinutes = int(input())
arrivingHour = int(input())
arrivingMinutes = int(input())

examTime = examHour * 60 + examMinutes
arrivingTime = arrivingHour * 60 + arrivingMinutes

finalHour = 0
finalMinutes = 0

if examTime >= arrivingTime:
    finalTime = examTime - arrivingTime
    finalHour = finalTime // 60
    finalMinutes = finalTime % 60
    if finalTime == 0:
        print("On time")
    elif finalTime <= 30:
        print("On time")
        print(f"{finalMinutes} minutes before the start")
    elif finalTime > 30:
        print("Early")
        if finalHour == 0:
            print(f"{finalMinutes} minutes before the start")
        elif finalHour > 0 and finalMinutes >= 10:
            print(f"{finalHour}:{finalMinutes} hours before the start")
        elif finalHour > 0 and finalMinutes < 10:
            print(f"{finalHour}:0{finalMinutes} hours before the start")
elif examTime < arrivingTime:
    finalTime = arrivingTime - examTime
    finalHour = finalTime // 60
    finalMinutes = finalTime % 60
    print("Late")
    if finalHour == 0:
        print(f"{finalMinutes} minutes after the start")
    elif finalHour > 0 and finalMinutes >= 10:
        print(f"{finalHour}:{finalMinutes} hours after the start")
    elif finalHour > 0 and finalMinutes < 10:
        print(f"{finalHour}:0{finalMinutes} hours after the start")