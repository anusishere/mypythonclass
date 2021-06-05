

#print(string.startswith("P"))

#print(string.endswith("shfshf"))

#conditionals
#and / or
# and - the two conditions must be true for the test to pass

# or - any of these conditions are true for the test to pass

age = 18
height = 4
movie  = "Scarry-terry"

if( age >= 18):
   print("This customer can purchase ticket for the movie " + movie )

if( age < 18):
   print("This customer cannot purchase ticket for the movie " + movie )

elif( age >= 18 and height >= 5):
    print("person can get on this ride") 

elif( age < 18 or height < 5):
    print("person cannot get on this ride")

else:
    print("Error, Something went wrong with your inputs")
