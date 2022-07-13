#  *****************************************************************************
#    FILE:        functions.py
#
#    AUTHOR:      {Your Name Here}
#
#    ASSIGNMENT:  Magic 8 Ball fortune teller and Eli's Shipping
#
#    DATE:         {Today's Date}
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************

# ELI's SHIPPING RATES
# Ground Shipping
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$1.50           |	$20.00
# Over 2 lb but less than or equal to 6 lb  |   $3.00           |	$20.00
# Over 6 lb but less than or equal to 10 lb |   $4.00           |	$20.00
# Over 10 lb                                |   $4.75           |	$20.00

# Ground Shipping Premium
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$0.00           |	$125.00
# Over 2 lb but less than or equal to 6 lb  |   $0.00           |	$125.00
# Over 6 lb but less than or equal to 10 lb |   $0.00           |	$125.00
# Over 10 lb                                |   $0.00           |	$125.00

# Drone Shipping
# Weight of Package                         | Price per Pound   | Flat Charge
# 2 lb or less                              |	$4.50           |	$0.00
# Over 2 lb but less than or equal to 6 lb  |   $9.00           |	$0.00
# Over 6 lb but less than or equal to 10 lb |   $12.00          |	$0.00
# Over 10 lb                                |   $14.25          |	$0.00

# Make sure to add parameters
import random


def fortune(name, question):
    amount_answers = random.randrange(1, 9)
    name_index = name.find(" ")
    first_name = name[0:name_index]
    if first_name[-1] == 's':
        print(f"{first_name}' question: {question}")
    else:
        print(f"{first_name}'s question: {question}")
    # print(amount_answers)
    if amount_answers == 1:
        print("Magic 8-Ball's answer: yes-definitely.")
    elif amount_answers == 2:
        print("Magic 8-Ball's answer: It is decidedly so.")
    elif amount_answers == 3:
        print("Magic 8-Ball's answer: Without a doubt.")
    elif amount_answers == 4:
        print("Magic 8-Ball's answer: Reply hazy, try again.")
    elif amount_answers == 5:
        print("Magic 8-Ball's answer: Ask again later.")
    elif amount_answers == 6:
        print("Magic 8-Ball's answer: Better not tell you now.")
    elif amount_answers == 7:
        print("Magic 8-Ball's answer: My sources says no.")
    elif amount_answers == 8:
        print("Magic 8-Ball's answer: Outlook not so good.")
    elif amount_answers == 9:
        print("Magic 8-Ball's answer: Very doubtful.")
    # print(name_index)
    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.


#  Make sure to add parameters
def shipping(weight):
    kilo_Pounds = 2.20
    lbs = kilo_Pounds * weight
    if lbs <= 2:
        ground_shipping = lbs * 1.50 + 20
        print(f"The price of ground shipping is $ {ground_shipping}") 
    elif lbs > 2 and lbs <= 6:
        ground_shipping = lbs * 3 + 20
        print(f"The price of ground shipping is $ {ground_shipping}") 
    elif lbs > 6 and lbs <= 10:
        ground_shipping = lbs * 4 + 20
        print(f"The price of ground shipping is $ {ground_shipping}") 
    elif lbs > 10:
        ground_shipping = lbs * 4.75 + 20
        print(f"The price of ground shipping is $ {ground_shipping}") 
    if lbs <= 2:
        ground_shipping_Premium = lbs * 0 + 125
        print(f"The price of premium ground shipping is $ {ground_shipping_Premium}")
    elif lbs > 2 and lbs <= 6:
        ground_shipping_Premium = lbs * 0 + 125
        print(f"The price of premium ground shipping is $ {ground_shipping_Premium}")
    elif lbs > 6 and lbs <= 10:
        ground_shipping_Premium = lbs * 0 + 125
        print(f"The price of premium ground shipping is $ {ground_shipping_Premium}")
    elif lbs > 10:
        ground_shipping_Premium = lbs * 0 + 125
        print(f"The price of premium ground shipping is $ {ground_shipping_Premium}")
    if lbs <= 2:
        drone_Shipping = lbs * 4.50 + 0
        print(f"The price of drone shipping is $ {drone_Shipping}")
    elif lbs > 2 and lbs <= 6:
        drone_Shipping = lbs * 9 + 0
        print(f"The price of drone shipping is $ {drone_Shipping}")

    elif lbs > 6 and lbs <= 10:
        drone_Shipping = lbs * 12 + 0
        print(f"The price of drone shipping is $ {drone_Shipping}")

    elif lbs > 10:
        drone_Shipping = lbs * 14.25 + 0 
        print(f"The price of drone shipping is $ {drone_Shipping}")
    if ground_shipping < ground_shipping_Premium and ground_shipping < drone_Shipping:
      print("To save the most money, you should choose ground shipping!")
    elif ground_shipping_Premium < ground_shipping and ground_shipping_Premium < drone_Shipping:
      print("To save the most money, you should choose ground shipping premium!")
    elif drone_Shipping < ground_shipping and drone_Shipping < ground_shipping_Premium:
      print("To save the most money, you should choose drone shipping!")
    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.


def main():
    name = input("What is your full name? ")
    question = input("What is your question you would like to answer? ")
    # fortune(name, question)
    weight = float(input("What is your package weight in kg? "))
    shipping(weight)

    # Collect user input in main and pass these values to the functions fortune and shipping.
    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.


##################DO NOT EDIT BELOW THIS LINE################
# This invokes the main function.  It is always included in our
# python programs.
if __name__ == "__main__":
    main()