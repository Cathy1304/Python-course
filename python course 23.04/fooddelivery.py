chicken = 10.35
fish = 12.4
vegetarian = 8.15
chickenMeal = int(input())
fishMeal = int(input())
vegetarianMeal = int(input())
chickenPrice = chickenMeal * chicken
fishPrice = fishMeal * fish
vegetarianPrice = vegetarianMeal * vegetarian
allPrice = chickenPrice + fishPrice + vegetarianPrice
discount = allPrice * 0.2
delivery = 2.5
Price = discount + allPrice + delivery
print(Price)
