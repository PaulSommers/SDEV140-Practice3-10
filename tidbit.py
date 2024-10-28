"""
Author: Paul Sommers
Date written: 10/28/2024
Assignment: Exercise 3-10
Short Desc: This program takes an input price from a user and calculates a payment schedule for a loan based on the price.
"""

# Constants
ANNUAL_RATE = 0.12
MONTHLY_RATE = ANNUAL_RATE / 12
DOWNPAYMENT_RATE = 0.10
TABLEFORMATSTRING = "{:2d}{:15.2f}{:15.2f}{:17.2f}{:17.2f}{:17.2f}"

# Have the user input a price
price = float(input("Enter the purchase price: "))

# Initialize variables
monthlyPayment = 0.05 * price
month = 1
balance = price - (price * DOWNPAYMENT_RATE)

# Output table heading
print("\nMonth  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

# Loop to calculate and display payments
while balance > 0:

    # If the monthly payment is greater than the balance, adjust the final payment
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0
    else:
        interest = balance * MONTHLY_RATE

    # Calculate principal and remaining balance
    principal = monthlyPayment - interest
    remaining = balance - monthlyPayment

    # Display the current month's payment details
    print(TABLEFORMATSTRING.format(month, balance, interest, principal, monthlyPayment, remaining))

    # Update balance and increment month
    balance = remaining
    month += 1