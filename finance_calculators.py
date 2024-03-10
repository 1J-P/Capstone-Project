"""
Pseudo code solution:

Import math library to code for formula calculations and create user menu with input.
User input should not be affected by capitalises and display error for incorrect option.
User input options for investment; simple and compond interest include formula display total to user. 
User input options for compound interest and  display to user total monthly repayments.
"""


# Print header for menu styling.
print("=" * 100) 


# Import needed library for formula.
import math

# Created user menu.
print("\t\t Welcome to the financial calculator")
print("Enter either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment\t - to calculate the amount of interest you'll earn on your investment")
print("bond\t\t - to caculate the amount you'll have to pay on a home loan")

# Calculator option in lowercase and removing spacing in wording from user input.
calc_type = input("\n Enter investment or bond: ").lower().replace(" ", "")

# Condtional statement and input for investment option.
if calc_type == "investment":
    deposit = float(input("Please enter deposit amount:\n"))
    interest_rate = float(input("Please enter interest rate as a number (e.g. 1, 2, 3) not 3%:\n"))
    n_year = float(input("Please enter the number of years you plan on investing:\n"))
    interest_type = input("Please enter 'simple' or 'compound' for investment type:\n")

    # Simple interest total printed to user.
    if interest_type == "simple":
        simple_interest = round(deposit*(1 + interest_rate * n_year/100))
        print(f"\n Your investment will be worth £{simple_interest} after {n_year} years. ")

    # Compond interest total printed to user.
    elif interest_type == "compound":
        compound_investment = round(deposit*math.pow((1 + interest_rate/100),n_year))
        print(f"\n Your investment will be worth £{compound_investment} after {n_year} years.")

    # prompting user to choose interest type if non of the options were met.    
    else:
        print("\n You have entered an invalid option.\n Please try again.")  

# Condtional statement and input for bond option.
elif  calc_type == "bond":
    house_value = float(input("\n Please enter present value of house: "))     
    rate = float(input("Please enter your interest rate as a number: "))
    n_month = float(input("Plesae enter the number of months bond will be repaid: "))

# Calculations for monthly percentage
    interest_rate = rate/100/12
    total_repayment = round(((interest_rate * house_value)/(1 - math.pow((1 + interest_rate), - n_month))),2)
    print(f"\n Your monthly bond repayment will be £{total_repayment:.2f}")

# Print message to user if non of the options have been selected. 
else:
    print("You have not entered a correct calculator type.") 
    

