import math

days = float(input())
room = input()
evaluation = input()

days -= 1

price = 0
final_price = 0
discount = 0
room_for_one_person = 18
apartment = 25
president_apartment = 35

if room == "room for one person":
    price = days * room_for_one_person

if room == "apartment":
    if days < 10:
        price = days * apartment
        discount = price * 0.3
        final_price = price - discount
    elif 10 <= days <= 15:
        price = days * apartment
        discount = price * 0.35
        final_price = price - discount
    elif days > 15:
        price = days * apartment
        discount = price * 0.5
        final_price = price - discount

if room == "president apartment":
    if days < 10:
        price = days * president_apartment
        discount = price * 0.1
        final_price = price - discount
    elif 10 <= days <= 15:
        price = days * president_apartment
        discount = price * 0.15
        final_price = price - discount
    elif days > 15:
        price = days * president_apartment
        discount = price * 0.2
        final_price = price - discount

if evaluation == "positive":
    if room == "room for one person":
        price += price * 0.25
        print(f"{price:.2f}")
    elif room == "apartment" or room == "president apartment":
        final_price += final_price * 0.25
        print(f"{final_price:.2f}")
elif evaluation == "negative":
    if room == "room for one person":
        price -= price * 0.1
        print(f"{price:.2f}")
    elif room == "apartment" or room == "president apartment":
        final_price -= final_price * 0.1
        print(f"{final_price:.2f}")
