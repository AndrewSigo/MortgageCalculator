# Mortgage Calculator
# Final project for CS101

# welcome meassage asking if user wants to continue
def welcome_message(welcome=input("Welcome to the Mortgage Calculator! Do you wish to coninue? Y/N: ")):
    if welcome == "Y":
        print("Great! Let us continue.")
    else:
        print("That's okay, maybe later.")


# takes user input to store values, then calculates the monthly payments
def payment_calculation():
    principle = input("What is the cost of the home?: ")
    intrest_rate = input("What is the intrest rate?: ")
    loan_term = input("How many years is the loan?: ")

    payment = (float(principle) * (float(intrest_rate) / 100)) / 1 - \
        (1 / (1 + float(intrest_rate)) ** int(loan_term))
    print(f"Your monthly principle payment is ${round(payment, 3)}")


welcome_message()
payment_calculation()
