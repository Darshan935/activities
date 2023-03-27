a = "Delux room"
b = "Non Ac room"

type_of_room = input("Which type of room did you book?\n  1. Delux Room\n  2. Non AC Room\n")

calculate_days = int(input("Enter the total number of days:\n"))
food_amount = float(input("Enter the total amount of food:\n"))

if type_of_room == "1":
    total_days = calculate_days * 7500
    total_food_price = food_amount * 1.18
    tip_amount = food_amount*0.1
    final=total_food_price+tip_amount
    final_amount= final+total_days
    print(f"You stayed in Delux Room for {calculate_days} days.")
    print("18% GST added on your food amount.")
    print("Extra 10% tip amount add in you bill")
    print("The total amount payable for a Delux Room is:", final_amount)
    print("Thankyou ,Have a nice day ")
elif type_of_room == "2":
    total_days = calculate_days * 4500
    total_food_price = food_amount * 1.05
    tip_food_price=food_amount*0.1
    final=total_food_price+tip_food_price
    final_amount = total_days + final
    print(f"You stayed in Non AC Room for {calculate_days} days.")
    print("5% GST added on your food amount.")
    print("Extra 10% tip amount add in you bill")
    print("The total amount payable for a Non AC Room is:", final_amount)
    print("Thankyou ,Have a nice day ")
else:
    print("Invalid room type selected!")
