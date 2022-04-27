# Mortgage Calculator
# Final project for CS101


def welcome_print(welcome=input("Welcome to the Mortgage Calculator! Do you wish to coninue? Y/N: ")):
    if welcome == "Y":
        print("Great! Let us continue.")
    else:
        print("That's okay, maybe later.")


welcome_print()
