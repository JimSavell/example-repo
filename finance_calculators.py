import math

# Describe the available selections for the user
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

#Asks user for what type of calulator they want
inv_bond = input("Please select investment or bond from the menu above: ").lower()

# Gathering information needed for investment and what type of interest
if inv_bond == "investment":
    deposit_amount = float(input("Please enter the amount you plan to deposit: "))
    interest_rate = float(input("Enter the interest rate: "))
    interest_rate = interest_rate / 100
    years_invested = float(input("Enter number of years you plan to invest: "))
    simple_compound = input("Is this for simple or compound interest: ").lower()

    #The calculations for simple and compound interest, displaying to user
    if simple_compound == "simple":
        total_amount = deposit_amount * (1 + interest_rate * years_invested)
        print(total_amount)
    else:
        total_amount = deposit_amount * math.pow((1 + interest_rate), years_invested)
        print(total_amount)

# Gathering information needed for bond calculations, calculate monthly payment 
# and display it to user
elif inv_bond == "bond":
    
    house_value = float(input("What is the present value of your house: "))
    house_rate = float(input("What is your current interest rate: "))
    repay_months = float(input("How many months will you take to repay bond: "))
    house_rate = (house_rate / 100) / 12
    
    repay_amount = (house_rate * house_value) / (1 - (1 + house_rate) ** (-repay_months))
    print(repay_amount)

else:
    print("Please try again.")
