class Student:

    def __init__(self):
            self. firstname = firstname
            self.lastname = lastname
            self.DOB = DOB
            self.major = major
            self.date = date
        

    def get_firstname():
        enter_firstname = input(" Enter your first name: ")
        return enter_firstname
 
    def get_lastname():
            enter_model = input(" Enter your last name: ")
            return enter_lastname

    def get_DOB():
            enter_DOB = input(" Enter your DOB : ")
            return enter_DOB

    def get_major():
            enter_major = input(" Enter your major: ")
            return enter_major

    def get_date():
            enter_date = input(" Enter today's date: ")
            return enter_date

def main():
    firstname = Student.get_firstname()
    lastname = Student.get_lastname()
    DOB = Student.get_DOB()
    major = Student.get_major()
    date = Student.get_date()

if __name__ == "__main__":
    main()
    
