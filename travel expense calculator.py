#travel expense system 

food_per_day = 50 
car_fuel_cost = 43

hotel_stay= input("What is the cost of your room?")
public_transport=input("What is the cost of your ticket")
days_stayed=input("How many days did you stay?")
miles_travelled= input("How many miles did you travel?")

hotel_costs=int(hotel_stay)
transport_costs=int(public_transport)
food_total=int(days_stayed)*food_per_day
fuel_total=(int(miles_travelled)*car_fuel_cost)/100

print(f"The costs incurred are as below:\nHotel stay = £{hotel_costs}\nFood = £{food_total}\nPublic transport = £{transport_costs}\nContribution to car fuel cost = £{fuel_total}")
total=hotel_costs+transport_costs+food_total+fuel_total
print(f"Total cost incurred is {total}")
