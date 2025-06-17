class Automobile:

    def __init__(make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def get_make():
        enter_make = input(" Enter make: ")
        return enter_make
 
    def get_model():
        enter_model = input(" Enter model: ")
        return enter_model

    def get_color():
            enter_color = input(" Enter color : ")
            return enter_color

    def get_year():
            enter_year = input(" Enter year : ")
            return enter_year

    def get_mileage():
            enter_mileage = input(" Enter mileage: ")
            return enter_mileage
def main():
    make = Automobile.get_make()
    model = Automobile.get_model()
    color = Automobile.get_color()
    year = Automobile.get_year()
    mileage = Automobile.get_mileage()

if __name__ == "__main__":
    main()



    
auto_list = []
name = ""
choice = "foobar"
OKCHOICES = "01234" 

while choice != "0":
    print
    print ("Menu: ")
    print ("1- Add Automobile")
    print ("2- Delete Automobile")
    print ("3- Update")
    print ("0- Exit")

    choice = "null"
    break

while choice not in OKCHOICES:
    choice = input("What would you like to do?: ")

if choice == "1":
    name = input("Please enter new automobile name")
    auto_list.append(name)
    print(name, "has been added.")
    name = ""

if choice == "2":
    name = input("Please enter automobile to delete")
    if name not in auto_list:
        print("Automobile not here.")

if choice == "3":
    if len(auto_list) == 0:
        print("No inventory.")
    else:
        print("Vehicle inventory:")
        for automobile in auto_list:
            print(automobile)
    
