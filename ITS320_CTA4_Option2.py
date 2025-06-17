#-------------------------------------------------------------------------------
#Program Name: Option #2: Repetition Control Structure- Grade Statistics
#Author: Erin Feltman
#Date: 03/13/22
#-------------------------------------------------------------------------------
#Pseudocode: 1. Initialize variable
#            2. Loop five times for 5 grades
#            3. Display the average, minimum, and maximum
#-------------------------------------------------------------------------------
#Program Inputs: 5 grades within the range of 0 - 100
#Program Outputs: The total, average, minimum, and maximum
#-------------------------------------------------------------------------------
Grade = 0
Number = 0
Counter = 0 #To count the numbers
Sum = 0
Average = 0
a_list = []
Minimum = 0
Maximum = 0
InputValue = ""
k = 0

print("Display average, minimum, and maximum of a set of grades")

InputValue = input("Please enter how many: ")
if InputValue == "":
    print("ERROR: How many must be supplied.")
else:
    if not (InputValue.isdigit()):
        print("ERROR: Grade must be supplied.")
    else:
        Grade = int(InputValue)
        if (Grade < 0) or (Grade > 100):
            print("ERROR: Grade must be between 0 an 100.")

for i in range(1, Grade+1):
    InputValue = input("Please enter grade: ")
    if InputValue == "":
         print("ERROR: Must enter grade. ")
    else:
        if not (InputValue.isdigit()):
            print("ERROR: Grade must be a number.")
        else:
            Number = int(InputValue)
            if (Number > 100) or (Number < 0):
                print("ERROR: Grade must be between 0 and 100.")
                
    while(Counter < 5):#Added a while loop
        Counter = Counter + 1
    Sum = Sum + Number
    Average = (Sum)/(Counter)
    Minimum = 9999
    Maximum = 0
    
    
print("Count of Numbers < 101: " + str(Counter))
print("Sum of all numbers: " + str(Sum))
print("The average of the grades are: ", Average)
print("The minimum of the grades is: ", Minimum)
print("The maximum of the grades is: ", Maximum)


print("End of program")


    
               














