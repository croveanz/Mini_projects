print("Hello, Welcome to the mortgage calculator")
while True:
    try:
        borrow_amount = abs(int(input("How much would you like to borrow? ")))
    except ValueError:
        print("Please enter a number ")
    else:
        break

while True:
    try:
        years = abs(int(input("How many years would you like the loan to be? ")))
    except ValueError:
        print("Please enter a number")
    else:
        break

while True:
    try:
        initial_interest = abs(float(input("Write your initial interest here ")))
    except ValueError:
        print("Please enter a number ")
    else:
        break


def compound_interest():
    try:
        print("Your compound interest is " + str(borrow_amount * (pow((1 + initial_interest/100),years))))
    except OverflowError:
        print("Number is too big to calculate the compund interest")

def monthly_payment():
    print("Your monthly payment is " + str((borrow_amount * initial_interest) / 12))

def total_interest_paid():
    print("Your total interest paid is " + str(borrow_amount * initial_interest * years))


compound_interest()
monthly_payment()
total_interest_paid()