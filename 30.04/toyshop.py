import math

price_of_trip = float(input())
puzzle = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
number_of_all = puzzle + dolls + bears + minions + trucks
price_of_all = (puzzle * 2.60) + (dolls * 3) + (bears * 4.1) + (minions * 8.2) + (trucks * 2)
discount = price_of_all * 0.25
if number_of_all >= 50:
    price_of_all = price_of_all - discount
else:
    price_of_all = price_of_all * 1
pechalba = price_of_all - (price_of_all * 0.1)
if pechalba >= price_of_trip:
    print(f"Yes! {pechalba - price_of_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_of_trip - pechalba:.2f} lv needed.")





