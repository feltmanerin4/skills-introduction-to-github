#-------------------------------------------------------------------------------
#Program Name: Option #2: List Computations
#Author: Erin Feltman
#Date: 03/27/22
#-------------------------------------------------------------------------------
#Pseaudocode: 1. define your two lists and the product because it uses the Cartesian product.
#             2. Each list needs a user input to enter up to 10 numbers
#             3. append the list to add list B to A
#             4. print
#-------------------------------------------------------------------------------
#Program Inputs: up to 10 numbers for each list
#Program Outputs: Cartesian product
#-------------------------------------------------------------------------------
inputA = []
InputB = []
user_input = 0
product = []

inputA = (input("Enter up to 10 numbers: "))
inputB = (input("Enter up to 10 numbers: "))

for a in inputA:
    for b in inputB:
        product.append((a, b))
        


print("The cartesian product is: ", product)

