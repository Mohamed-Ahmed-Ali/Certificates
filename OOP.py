# A class is an extensible program-code-template for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods).
class Student:  
# Student is the name of the Class (Student is an Object)
# Object is an instance of a class, That is, an object is a member of a given class with specified values rather than variables.
    graduate = True                     # Class Variable
    Military_Duty = "Done"              # Class Variable
    def __init__(self, name, course):   # Constructor Method - called when object created. self refers to the current instance of the class    
    # name and course is the object ATTRIBUTE (The Variables related to the Object)
        self.name = name                # Instance Variable
        self.course = course            # Instance Variable
    # The method is a function that is associated with an object. In Python, a method is not unique to class instances. Any object type can have methods.
    def attend(self):                   # attend Method
        print("This Student is attend")
    def absent(self):                   # absent Method
        print("This Student is absent")

def get_student():
    name = input("Name: ")
    course = input("Course: ")
    student = Student(name, course)
    return student

def main():
    student = get_student()
    print(f"{student.name} from {student.course}")


# Object is an instance of a class 

# Struct before object because no method

# Class : الفئه هي حد (أطار) الشئ او تعريغه > العائله الصفة العامه
# Object : الشئ هو نمزج من الفئه < فرد من العئله لهو صفة خاصة
# Method : وضيفة الفرد (Function)
# Attribute : صفة الفرد (Instance Variables)



# Abstraction : a programmer hides all but the relevant data about an object in order to reduce complexity and increase efficiency.
    # Encapsulation : Setters & Getters Black box

# Inheritance : Parent & Child Relation
    # Polymorphism : Same Method in parent class but different behavior (Method Definition) Through Method OverRiding & Method OverLoading
        # ● Method OverRiding : The Same Method nut different Behaver for every Class
        # ● Method OverLoading : Repeat the same function with the Same but Different Parameters to out put slightly different Output