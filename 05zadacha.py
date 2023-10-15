PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
CLEANING_MATERIAL_PRICE = 1.20

pens_count = int(input())
marker_count = int(input())
cleaning_material_count = int(input())
discount_percent = int(input())


total_sum = pens_count * PENS_PRICE + marker_count * MARKERS_PRICE + cleaning_material_count * CLEANING_MATERIAL_PRICE

total_sum_discount = total_sum * (100 - discount_percent) / 100

print(total_sum_with_discount)