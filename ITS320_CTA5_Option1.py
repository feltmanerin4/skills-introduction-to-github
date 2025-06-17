#-------------------------------------------------------------------------------
#Program Name: Option #1: String Values in Reverse Order
#Author: Erin Feltman
#Date: 3/20/22
#-------------------------------------------------------------------------------
#Pseudocode: 1. Obtain input from the user. Have it loop three times.
#            2. Define a function that contains the three strings. 
#            3. Take those three outputs and concatenate them together with plus signes.
#            4. Have it print out the three values in reverse.
#-------------------------------------------------------------------------------
#Program Inputs: "Please enter a string value"
#Program Outputs: The three strings with the third letter in reverse order
#-------------------------------------------------------------------------------
count = 0

def ReverseString(One1, Two2, Three3):
    Average = 0.0
    Average = (One1 + Two2 + Three3)
    return Average

One = str(input("Please enter a string: "))
Two = str(input("Please enter a string: "))
Three = str(input("Please enter a string: "))

print(str(ReverseString(One, Two, Three)))
print(Three[::-1])
print(min(One, Two, Three))
print(max(One, Two, Three))    


print("End of program")


        
