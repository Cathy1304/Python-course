packagePaperPrice = 5.80
textilePrice = 7.20
gluePrice = 1.20

packageAmount = int(input())
textileAmount = int(input())
glueAmount = float(input())

discount = float(input()) / 100

packageTotal = packagePaperPrice * packageAmount
textileTotal = textilePrice * textileAmount
glueTotal = gluePrice * glueAmount

moneyNeeded = (packageTotal + textileTotal + glueTotal) * (1 - discount)

print(f"{moneyNeeded:.3f}")