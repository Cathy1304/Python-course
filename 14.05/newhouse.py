import math

def main():
    # Input
    flowers_type = input()
    flowers_quantity = int(input())
    budget = int(input())

    # Prices
    roses_price = 5 * flowers_quantity
    dahlias_price = 3.80 * flowers_quantity
    tulips_price = 2.80 * flowers_quantity
    narcissus_price = 3 * flowers_quantity
    gladiolus_price = 2.50 * flowers_quantity
    total_price = 0

    if flowers_type == "Roses":
        total_price = roses_price

        if flowers_quantity > 80:
            total_price *= 0.9

    elif flowers_type == "Dahlias":
        total_price = dahlias_price

        if flowers_quantity > 90:
            total_price = dahlias_price * 0.85

    elif flowers_type == "Tulips":
        total_price = tulips_price

        if flowers_quantity > 80:
            total_price = tulips_price * 0.85

    elif flowers_type == "Narcissus":
        total_price = narcissus_price

        if flowers_quantity < 120:
            total_price = narcissus_price * 1.15

    elif flowers_type == "Gladiolus":
        total_price = gladiolus_price

        if flowers_quantity < 80:
            total_price = gladiolus_price * 1.20

    if budget >= total_price:
        money_left = budget - total_price
        print(f"Hey, you have a great garden with {flowers_quantity} {flowers_type} and {money_left:.2f} leva left.")
    else:
        money_needed = total_price - budget
        print(f"Not enough money, you need {math.fabs(money_needed):.2f} leva more.")
if __name__ == "__main__":
    main()
