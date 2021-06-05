import datetime
import math
database ={}
balance = 100
def basicMenu():
    print('These are the available options')
    print('1. Withdrawl')
    print('2. Deposit')
    print('3. Comlpaint')
    selectedOption = int(input('Please selct an opton: '))
    return selectedOption

def option(choice):
    global balance
    if(choice == 1):
        print('You selected %s' % choice)
        print('How much would you like to withdraw? \n')
        withdraw = int(input())
        if( withdraw > balance):
            print("Error: withdrawl money is more than the balance.")
        elif(balance == 0):
            print("Error:No money in the bank. Pls, deposit first.")
        balance -= withdraw
        print('Balance :  %d' , balance )
        print('Take your cash')
        basicMenu()
    elif(choice == 2):
        print('You selected  %d' % choice)
        print("How much would you like to deposit? ")
        deposit = int(input()) 
        balance += withdraw
        print('Balance :  %d' , balance )
        basicMenu()
    elif(choice == 3):
        print('You selected %d ' % choice)
        print('What issue would you like to report? \n')
        complaint = input()
        print('"Thank you for contacting us."')
        basicMenu()
    else:
        print('Inavlaid option. Try again')
        basicMenu()

#allowedUsers = ['Anu', 'Mike', 'John']
#allowedPassword = ["passwordAnu", "passwordMike", "passwordJohn"]
#amounts = [5000, 4000, 3000]
#name = input("what is your name? \n")
#userId = allowedUsers.index(name)

datetime_string = str(datetime.datetime.now())
print( ' ' + name + 'logged in on ATM_Mock_Project on ' + datetime_string) 
#if(name in allowedUsers):
#   userId = allowedUsers.index(name)
 #  password = input( "Your password? \n")
#   if(password == allowedPassword[userId]):
#      print('Welcome %s' % name )
#      print(datetime_string)
#      basicMenu()  
#   else:
#       print('Password Incorrect, please try again')
#else:
 #   print('Name not found. Please try again')


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
    is_valid_account_number = (account_number_from_user).isdecimal()
    if is_valid_account_number:
        password = input('what is your password? \n')
        user = database.authenticated_user(account_number_from_user, password)
        if user:
            bank_operation(user)
        print('Invalid account or password')
        login()

    else:
        print('Your account number is not valid. Please recheck again next time')
        init()

def register():
    print('******** Register **********')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create password for yourself \n')
    #balance = int(input('How much money you want to put into the bank now? \n'))
    account_number = generation_account_number()
    is_user_created = database.create(account_number, first_name, last_name, email, password, str(0))
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


    
