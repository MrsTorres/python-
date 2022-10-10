
import string
import random

#declare variables
number_of_instances=int  #the number of instances user will request
Departments=['Marketing','Accounting','FinOps']  #declaring the names of the departments 
instance_name_list=[]  #list of random generatored ids
inputMessage="\nType in your choice: "  #display text for input 

#defining the functions based off the user input
def verifyList(usrInput,ValidateList):
    while usrInput not in ValidateList:
        print('\ninvalid entry, please check spelling and try again:\n*Departments are case sensitive!\n')
        usrInput=input(inputMessage)
    else:  
        return usrInput
    
#defining a random name generator that has up to 4 unique characters after the department name, and requires uppercase 
def randomIDgenerator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print ("Enter department name you wish to create an instance for?\nYour options are:(Department names are case sensitive)\n")

#For loop to iterate department list indexes and display/print a numbered list 

length=len(Departments) #declaring the length of departments, value=departments which are 3
for i in range(length): #for index in range of length which is 3, the following is going to happen
    number=i+1  #declaring number to equal the index plus 1
    print(number,'-',Departments[i]) #display the above function, number list and departments 

#get user input, info is verified through the verifyList function,once validated info is passed onto departments variable
department=verifyList(input(inputMessage),Departments)

#exception error is raised if user doesnt enter an interger, and looping until the correct value is entered
while True:
    number_of_instances = input('\nHow many unique instance names would you like to generate for this department?:\n')

    try: 
        int(number_of_instances)
    except ValueError:
        print('\nThe value you entered is not a number\n')
    else:   
        int(number_of_instances)
        break
    
# For loop that iterates according on the number of instance IDs user requested, 
# each iteration will add a unique name to each index on the list based on index range (numbers of iterations).

for i in range(int(number_of_instances)):#r if instances input by user
    instance_name_list.append(department+randomIDgenerator())

# Declare length variable, inherits value based on the lenth of the instance_name_list
length=len(instance_name_list)  

# For loop iterates index according to the ther number of length value
for i in range(length):
    print('\n'+ instance_name_list[i]) # display unique IDs 
    

    



    





