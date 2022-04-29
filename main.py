# Mortgage Calculator
# Final project for CS101

# welcome meassage asking if user wants to continue
def welcome_message(welcome=input("Welcome to the Mortgage Calculator! Do you wish to coninue? Y/N: ")):
    if welcome == "Y":
        print("Great! Let us continue.")
    else:
        print("That's okay, maybe later.")


welcome_message()

# stores user input to variables to be used later to calculate payments


def user_info():
    principle = input("What is the cost of the home?: ")
    intrest_rate = input("What is the intrest rate?: ")
    loan_term = input("How many years is the loan?: ")
    print(principle, loan_term, intrest_rate)
    # print(principle)
    # print(intrest_rate)
    # print(loan_term)


# user_info()
# trying to call user_info and use the variables in the formula
def payment_calculation():
    user_info()
    payment = (principle * intrest_rate) / 1 - \
        (1 / (1 + intrest_rate) ** loan_term)
    return f"Your monthly payment is {payment}."


print(payment_calculation())
