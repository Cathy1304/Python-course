import math

month = input()
nights = float(input())

studioMO = 50
ApartmentMO = 65
studioJniS = 75.20
ApartmentJniS = 68.70
studioJA = 76
ApartmentJa = 77
priceStudio = 0
priceApartment = 0

if month == "May" or month == "October":
    if nights <= 7:
        priceStudio = studioMO
        priceApartment = ApartmentMO
    elif nights > 7 and nights <= 14:
        priceStudio = studioMO * 0.95
        priceApartment = ApartmentMO
    elif nights > 14:
        priceStudio = studioMO * 0.70
        priceApartment = ApartmentMO * 0.9
elif month == "June" or month == "September":
    if nights >= 15:
        priceStudio = studioJniS * 0.80
        priceApartment = ApartmentJniS * 0.9
    elif nights < 15:
        priceStudio = studioJniS
        priceApartment = ApartmentJniS
elif month == "July" or month == "August":
    if nights >= 15:
        priceStudio = studioJA
        priceApartment = ApartmentJa * 0.90
    elif nights < 15:
        priceStudio = studioJA
        priceApartment = ApartmentJa

print(f"Apartment: {priceApartment * nights:.2f} lv.")
print(f"Studio: {priceStudio * nights:.2f} lv.")