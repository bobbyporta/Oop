class Students:
    def __init__(self, name, age, course):
       
        self.name = name
        self.age = age
        self.course = course
    
    def introduce1(self): # This method belongs to student1 object
        
        print(f"Student 1: Hi I am {self.name}, {self.age} years old and I am currently taking {self.course}.")
        print("")
    
    def introduce2(self): # This method belongs to student2 object
        
        print(f"Student 2: Hi I am {self.name}, {self.age} years old and I am currently taking {self.course}.")
        print("")
    
    def introduce3(self): # This method belongs to student3 object
        
        print(f"Student 3: Hi I am {self.name}, {self.age} years old and I am currently taking {self.course}.")
        print("")


if __name__ == "__main__":
    print("Info:")
    
    
    student1 = Students("Bobby", 22, "Diploma in Information Technology")
    student1.introduce1()
    
    student2 = Students("John", 20, "Bachelor of Science in Computer Science")
    student2.introduce2()
    
    student3 = Students("Erika", 20, "Bachelor of Elementary Education")
    student3.introduce3()
