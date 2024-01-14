import Subject

class Student(self , first_name,last_name,number):
    def __init__(self,first_name,last_name,number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.__grades = []

    def __init__(self,first_name, last_name, number, grades):
        self.__init__(first_name, last_name, number)
        self.__grades = grades



    def add_gradeS(self,grades):
        self.__grades.extend(grades)  

    def get_avg_grades_1():
        print ('test')    