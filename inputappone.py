import datetime
import math

def basicMenu():
    print('These are the available options')
    print('1. Cash Deposit')
    print('2. Withdrawl')
    print('3. Comlpaint')
    selectedOption = int(input('Please selct an opton: '))

    if(selectedOption == 1):
        print('You selected %s' % selectedOption)
        print('How much would you like to deposit? \n')
        deposit = int(input(prompt))
        balance += deposit
        print('Balance :  %d' , balance )
    elif(selectedOption == 2):
        print('You selected  %d' % selectedOption)
        print("How much would you like to withdraw? ")
        withdraw = int(input(prompt))
        balance -= withdraw
    elif(selectedOption == 3):
        print('You selected %d ' % selectedOption)
        print('What issue would you like to report? \n')
        complaint = input()
        print('"Thank you for contacting us."')
    else:
        print('Inavlaid option. Try again')

allowedUsers = ['Anu', 'Mike', 'John']
allowedPassword = ["passwordAnu", "passwordMike", "passwordJohn"]
name = input("what is your name? \n")
userId = allowedUsers.index(name)
x= datetime.datetime.now()
if(name in allowedUsers):
   userId = allowedUsers.index(name)
   password = input( "Your password? \n")
   if(password == allowedPassword[userId]):
      print('Welcome %s' % name )
      print(x)
      basicMenu()  
   else:
       print('Password Incorrect, please try again')
else:
    print('Name not found. Please try again')



    
