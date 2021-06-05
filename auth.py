#auth.py
#register
#first_name, last_name , password and email
#generate user account no


#login
#( username or email) and password

#bank operations

#Initialising the syatem
import random

database ={}  #dictionary

#initializing account
def init():
    isValidOptionSelected = False
    print("Welcome to bankPython!") 

    while isValidOptionSelected == False:
        haveAccount = int(input("Do you have account with us: 1(yes) and 2(no) \n"))
        if haveAccount ==1:
           login()
        elif haveAccount == 2:
           print(register())
        else:
          print("You have selected invalid option")
          init()
         

def login():
    print("*************** Login **************")
    accountNumberFromUser = int( input("what is your account number? \n"))
    password = input("what is your password  \n")
    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3]) == password):
               bankoperation(userDetails)
    print('Invalid account or password')          
    


def register():
    print("******** Register **********")
    email = input("What is your email address?  \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name?\n")
    password = input("Create password for yourself \n")
    accountNumber = generationAccountNumber()
    database[accountNumber] = [ first_name, last_name, email, password]
    #return database
    print("Your account has been created")
    print("== ==== ====== ==== ==")
    print("your account no is %d" % accountNumber)
    print("Make sure you keep it safe and remember")
    print("== ==== ====== ==== ==")
    login()


def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    
    SelectedOption = int(input("What would you like to do? (1) deposit (2) withdrawl (3) Logon (4) Exit"))
       
    if( selectedOption == 1):   
        depositOperation() 
    elif(selectedOption == 2):
        withdrawlOperation()
    elif(selectedOption == 3):
        logout()
    elif(selectedOption == 4):
        exit()
    else:
        print("You have selcted invalid option")
        bankOperation(user)
    

def withdrawlOperation():
    print("Withdrawl")

def depositlOperation():
    print("deposit operation")

def generationAccountNumber():
    print("Generating account number.") 
    return random.randrange(1111111111, 9999999999) 

def logout():
    login()

############### Actual Banking System #######
init()
    