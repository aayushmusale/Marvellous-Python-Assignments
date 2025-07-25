class Student:
    school_name = "ABC International School"
    # Accessing Class variable in Instance Method 2 methods : using 'self' and using 'class name'
    # always use class name
    # also while modifying class_variable name using 'self.class_variable' it creates a new instance variable instead of modifying the existing class_variable

    def __init__(self, name, rollNo):
        self.Name = name
        self.roll_no = rollNo

    def DisplayDetails(self):
        print("Name : ", self.Name)
        print("Roll Number : ", self.roll_no)
        print("School Name : ", Student.school_name)
    
    def changeSchool(self, school):
        Student.school_name = school
        # self.school_name = school
        print("School name changed to ", school)
    

def main():
    obj = Student('Aayush', 13)
    obj.DisplayDetails()
    obj.changeSchool('Marvellous Schoool Of Technology')
    obj.DisplayDetails()

if __name__ == "__main__":
    main()