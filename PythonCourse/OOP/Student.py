import Subject

class Student():
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.__gradesOfSubjects = []

    def add_gradeS(self, grades):
        self.__gradesOfSubjects.extend(grades)
    
    def get_avg_grades_for_sport_collages(self):
        total_sum = 0
        for subject in self.__gradesOfSubjects:
            if (subject.name == "Running" or subject.name == "Fitness"):
                total_sum +=  sum(subject.grades) / len(subject.grades)
        
        return total_sum / 2
