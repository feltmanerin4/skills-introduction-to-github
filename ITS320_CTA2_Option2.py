#----------------------------------------
#Program name: Option #2 Create a Python Application
#Author: Erin Feltman
#Date: 2/27/22
#----------------------------------------
#Pseaudocode:
#1. Make a dictionary that the user will need to fill out
#2. Print out the contents of the dictionary
#----------------------------------------
#Program Inputs:
#Enter the car brand:, enter the car model, enter the car year, enter the starting odometer reading, enter the ending odometer reading, enter the estimated mpg consumed by the vehicle
#Program Outputs:
#When the user populates the information from the above input with data.
#----------------------------------------
thecar = {
    "brand" : input("Enter the car brand: "),
    "model" : input("Enter the car model: "),
    "year" : input("Enter the car year: "),
    "Odostart" : input("Enter the car's starting odometer reading: "),
    "Odoend" : input("Enter the car's ending odometer reading: "),
    "mpg" : input("Enter the car's estimated mpg consumed by the vehicle: ")
    }
print(thecar)
