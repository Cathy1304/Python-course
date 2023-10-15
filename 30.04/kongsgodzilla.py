movie_budget = float(input())
mutes_number = int(input())
clothing_price = float(input())

decor_price = 0.10 * movie_budget
total_clothing_price = clothing_price * mutes_number

if mutes_number > 150:
    total_clothing_price = total_clothing_price - (0.10 * total_clothing_price)

total_money = total_clothing_price + decor_price
money_left = movie_budget - total_money

if total_money > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} leva more.")
elif total_money <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")