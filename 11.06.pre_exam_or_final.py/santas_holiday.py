rest_days = int(input())
type_of_room = input()
positive_or_negative = input()

price_for_room = 0
sum = 0

if type_of_room == "room for one person":
    price_for_room = 18.00
    sum = (rest_days - 1) * price_for_room
elif type_of_room == "apartment":
    price_for_room = 25.00
    sum = (rest_days - 1) * price_for_room
    if rest_days < 10:
        sum *= 0.7
    elif 10 <= rest_days <= 15:
        sum *= 0.65
    elif rest_days > 15:
        sum *= 0.5
elif type_of_room == "president apartment":
    price_for_room = 35.00
    sum = (rest_days - 1) * price_for_room
    if rest_days < 10:
        sum *= 0.9
    elif 10 <= rest_days <= 15:
        sum *= 0.85
    elif rest_days > 15:
        sum *= 0.8

if positive_or_negative == "positive":
    sum *= 1.25
elif positive_or_negative == "negative":
    sum *= 0.9

print(f"{sum:.2f}")