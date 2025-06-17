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



    

