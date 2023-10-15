import math

budget = int(input())
season = input()
fishermanNum = int(input())

boatPrice = 0
if season == "Spring":
    boatPrice = 3000
elif season == "Summer" or season == "Autumn":
    boatPrice = 4200
elif season == "Winter":
    boatPrice = 2600

if fishermanNum <= 6:
    boatPrice = boatPrice - (boatPrice * 0.10)
elif fishermanNum > 7 and fishermanNum <= 11:
    boatPrice = boatPrice - (boatPrice * 0.15)
elif fishermanNum > 12:
    boatPrice = boatPrice - (boatPrice * 0.25)

if fishermanNum % 2 == 0 and season != "Autumn":
    boatPrice = boatPrice - (boatPrice * 0.05)

if budget >= boatPrice:
    print(f"Yes! You have {math.fabs(budget - boatPrice):.2f} leva left.")
else:
    print(f"Not enough money! You need {math.fabs(budget - boatPrice):.2f} leva.")