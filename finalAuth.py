# finalAuth.py
#register
#username , password and email
#generate user account no
#bank operations
#initialising the system

import random

database ={} #dictionary

#login
#( username or email) and password

#initializing account
def init():
    isValidOptionSelected == False
    print("Welcome to bankPHP!") 

    while isValidOptionSelected == False:
       haveAccount = int(input("Do you have account with us: 1(yes) and 2(no) \n"))
    if(haveAccount ==1):
        isValidOptionSelected = True
        logout()
    elif(haveAccount == 2):
        isValidOptionSelected = True
        register()
    else:
        print("You have selcted invalid option")

def login():
    print("***** Login *****")
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        accountNumberFromUser = int( input("What is your Account Number \n"))
        password = input( "What is your password  \n")

        for accountNumber, userDetails in database.items():
            if( accountNumber == accountNumberFromUser):
                if(userDetails[3] == password ):
                    isLoginSuccessful = True
                    bankOperation(userDetails)
    print('Invalid account or password') 
    bankOperation()

def register():
    print("****** Register ******")
    email = input("What is your email address:  \n")
    first_name = input("what is your first name? \n")
    last_name = input( "What is your last name?  \n")
    password =  input("Create a pssword for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name,last_name, email, password, ]
    print("Your account has ben created")
    print("============================")
    print("Your account number is: %d " % accountNumber )
    print("Make sure you keep it safe")
    print("============================")
    
    login()

def bankOperation(user):
    print("Welcome %s  %s " % ( user[0], user[1]) )
    selectedOption = input( "What would you like to do? (1)deposit (2)withdrawl  (3)logout (4)exit \n")
    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawOperation()
    elif(selectedOption == 3): 
        login()
    elif(selectedOption == 4):  
        exit()    
    else:
        print("Invalid option selected\n") 
        bankOperation(user)

def withdrawOperation():
    print("withdraw")

def depositOperation():
    print("deposit")



def generationAccountNumber():
    print("Account number generator.")  

def logout():
    login()



############### Actual Banking System #######
init()
    