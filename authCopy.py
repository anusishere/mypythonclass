# authCopy.py and ATM Mock Up file too.
# authCopy.py written in pyCharm where if condition doesnt need curly braces
# register
# first_name, last_name , password and email
# generate user account no


# login
# ( username or email) and password

# bank operations


# Initialising the system
import random  # generates a pseudo random number between the range mentioned in curly braces
#from databases import Database

import validation
import database

# getpass function prints a prompt then reads input from the user until
# they press return and the input is passed back as a string
import getpass

account_number_from_user = None


# initializing account


def init():
    print('Welcome to BankPython!\n')
    have_account = int(input('Do you have account with us: 1(yes) and 2(no)\n'))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('You have selected invalid option\n')
        init()


def login():
    global account_number_from_user
    print('*************** Login **************')
    account_number_from_user = int(input('what is your account number? \n'))
    is_valid_account_number = validation.account_number_validation(account_number_from_user)
    if is_valid_account_number:
        password = input('what is your password? \n')
        user = database.authenticated_user(account_number_from_user, password)
        if user:
            database.login_auth_session( account_number_from_user, user)
            bank_operation(user)    
        print('Invalid account or password')
        login()

    else:
        print('Account number Invalid: Recheck that you have 10 digits and only integers')
        init()


def register():
    print('******** Register **********')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create password for yourself \n')
    #balance = int(input('How much money you want to put into the bank now? \n'))
    account_number = generation_account_number()
    is_user_created = database.create(account_number, first_name, last_name, email, password)
    if is_user_created:
        print('Your account has been created')
        print('== ==== ====== ==== ==')
        print('your account no is %d' % account_number)
        print('Make sure you keep it safe and remember')
        print('== ==== ====== ==== ==')
        login()
    else:
        print('Something went wrong. Please retry!')
        register()


def bank_operation(user):
    print('Welcome %s %s ' % (user[0], user[1]))

    selected_option = int(input('What would you like to do? (1) deposit (2) withdraw (3) Logout (4) Exit \n'))

    if selected_option == 1:
        deposit_operation(user)
    elif selected_option == 2:
        withdraw_operation(user)
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        exit()
    else:
        print('You have selected invalid option')
        bank_operation(user)


def withdraw_operation(user):
    print("************ Withdrawing *********")
    current_balance = int(get_current_account_balance(user))
    amount_to_withdraw = int(input('How much do you want to withdraw now? \n'))
    current_balance -= amount_to_withdraw
    set_current_account_balance(user, str(current_balance))

    if database.update(account_number_from_user, user):
        print('==== Current Bal: %d' % current_balance)
        print('Your current balance is {}'.format(current_balance))
        bank_operation(user)

    else:
        print('The transaction is not successful')
        bank_operation(user)

    print('Current balance: %d\n' % user[4])

    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount from current balance
    # display current balance


def deposit_operation(user):
    
    current_balance = int(get_current_account_balance(user))
    amount_to_deposit = int(input("How much do you want to deposit? "))
    current_balance += amount_to_deposit
    set_current_account_balance(user, str(current_balance))

    if database.update(account_number_from_user, user):
        print("Your account balance is {}".format(current_balance))
        bank_operation(user)
    
    else:
        print("Transaction not successful")
        bank_operation(user)

    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # update the user file with the new balance
    # display current balance


def generation_account_number():
   print('Generating account number.')
   return random.randrange(1111111111, 9999999999)


def set_current_account_balance(user_details, balance):
    user_details[4] = balance


def get_current_account_balance(user_details):
    return user_details[4]


def logout():
    login()


init()
