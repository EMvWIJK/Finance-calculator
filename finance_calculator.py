import math


print('''Investment      - to calculate the amount of interest youll earn on your investment.
bond            - to calculate the amount you'll have to pay on a home loan.''')

selection = str(input("\nEnter either 'investment' or 'bond' from the menu above to proceed:\n"))
choice = selection.lower()
print(choice)

#When investment is selected

if choice == "investment" :
    deposit = int(input("Enter the amount you are depositing: \n"))
    rate = int(input("Enter the interest rate (%): \n"))     
    years = int(input("Enter the amount of years: \n"))
    interest_choice = input("Select either 'simple' or 'compound' interest: \n")
    interest = interest_choice.lower()

    if interest == "simple" :
        total_interest = deposit*(1 + (rate/100) * years)
        simple_interest = round(total_interest, 2)
        print(simple_interest)

    elif interest == "compound" : 
        total_interest = deposit * math.pow((1+ (rate/100)),years)
        compound_interest = round(total_interest,2)
        print(compound_interest)

    else : 
        print("Invalid selection, try again")

#When bond is selected

elif choice == "bond" :
    value = int(input("Enter the current value of the house: \n"))
    rate = int(input("Enter the interest rate (%): \n"))
    months = int(input("Enter the amount of months to finish payment of the house: \n"))
    monthly_rate = (rate/100) / 12

    repay = (((monthly_rate) / 12) * value)/(1 - (1 + monthly_rate) ** (-months))
    repayment = round(repay,2)
    print(repayment)

#when user enters an invalid selection

else :
    print("Invalid selection, try again")