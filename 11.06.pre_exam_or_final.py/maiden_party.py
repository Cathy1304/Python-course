party_price = float(input())
love_messages = int(input())
wax_roses = int(input())
keychains = int(input())
cartoons = int(input())
lucky_surprises = int(input())

love_message_price = 0.60
wax_rose_price = 7.20
keychain_price = 3.60
cartoon_price = 18.20
lucky_surprise_price = 22.00

total_price = (love_messages * love_message_price) + (wax_roses * wax_rose_price) + \
              (keychains * keychain_price) + (cartoons * cartoon_price) + \
              (lucky_surprises * lucky_surprise_price)

if love_messages + wax_roses + keychains + cartoons + lucky_surprises >= 25:
    total_price *= 0.65

total_price -= total_price * 0.10

if total_price >= party_price:
    remaining_money = total_price - party_price
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    money_needed = party_price - total_price
    print(f"Not enough money! {money_needed:.2f} lv needed.")