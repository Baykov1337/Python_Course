from Student import Student
from Subject import Subject

studentPesho = Student("Pesho", "Ivanov", 123)
studentJohn = Student("John", "Dow", 321)
studentAlex = Student("Alex", "Petrov", 444)

peshoGrades = [Subject("Fitness", [2,3,4]), Subject("Math", [2,2,2,2])]
studentPesho.add_gradeS(peshoGrades)

johnGrades= [Subject("Fitness", [2,3,4]), Subject("Running", [6])]
studentJohn.add_gradeS(johnGrades)

alexGrades = [Subject("Egnlish", [2,3,4]), Subject("Math", [2,2,2,2])]
studentAlex.add_gradeS(alexGrades)

all_students = [studentPesho, studentJohn, studentAlex]

for s in all_students:
    if (s.get_avg_grades_for_sport_collages()) > 3:
        print(f"Mr {s.last_name} is accepted in or collage" )
    else:
        print(f"Mr {s.last_name} is not accepted" )

