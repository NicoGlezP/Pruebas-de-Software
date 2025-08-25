'''Function #1'''
def check_num(num):
    if num.isnumeric():
        print("Invalid")
    elif num > 0:
        print("Positive")
    elif num == 0:
        print("Zero")
    elif num < 0:
        print("Negative")

'''Function #2'''
def check_password(password):
    if password.len < 8:
        print("The password must be at least 8 characters long.")
    '''Continues'''

'''Function #3'''
def check_disc(amount):
    if amount < 100:
        print("No discount")
    elif amount >= 100 and amount <= 500:
        print("10%")
    elif amount > 500:
        print("20%")
    else: print("Invalid")


check_num("Hola")
check_disc(900)