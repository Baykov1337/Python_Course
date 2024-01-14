class Subject():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def add_grade(self, grade):
        self.grades.append(grade)
