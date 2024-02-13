import sqlite3
from Employee import Employee

conn = sqlite3.connect('test.sqlite')
#conn = sqlite3.connect(':memory:')
cur = conn.cursor()

cur.execute('delete from Employee')
conn.commit()
cur.execute('drop table Employee')
conn.commit()


cur.execute("""create table if not exists Employee 
            (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name text, 
                Position text, 
                Salary integer, 
                Status text
            )""")

conn.commit()

emp_1 = Employee('John Doe', 'Developer', 20000, 'Active')
emp_2 = Employee('Jane Doe', 'Manager', 40000, 'Active')

# print (emp_1.Name)
# print (emp_1.Position)
# print (emp_1.Salary)
# print (emp_1.Status)

cur.execute("insert into Employee (Name, Position, Salary, Status) values (?,?,?,?)", (emp_1.Name, emp_1.Position, emp_1.Salary, emp_1.Status ))
conn.commit()

cur.execute("insert into Employee (Name, Position, Salary, Status) values (:Name, :Position, :Salary, :Status)", {'Name':emp_2.Name,'Position':emp_2.Position, 'Salary': emp_2.Salary, 'Status':emp_2.Status })
conn.commit()

# cur.execute("select * from Employee")

# print(cur.fetchall())

# #1st method
# cur.execute("select * from Employee where name='Jane Doe'")

# print(cur.fetchall())
# #2nd method
# cur.execute("select * from Employee where name=?",('Jane Doe',))

# print(cur.fetchall())
# #3nd method


def insert_emp(emp):
    with conn:
        cur.execute("insert into Employee (Name, Position, Salary, Status) values (:Name, :Position, :Salary, :Status)", {'Name':emp.Name,'Position':emp.Position, 'Salary': emp.Salary, 'Status':emp.Status })

def update_salary(emp, Salary):
    with conn:
        cur.execute("update Employee set Salary = :Salary where name = :Name and Position = :Position", {'Name':emp.Name,'Position':emp.Position, 'Salary': Salary})

def remove_emp(emp):
    with conn:
        cur.execute("delete from Employee where name = :Name and Position = :Position", {'Name':emp.Name,'Position':emp.Position})

def get_emp(emp):
    with conn:
        cur.execute("select * from Employee where name= :Name",{'Name': emp})
        return cur.fetchall()

emp_1 = Employee('John Doe', 'Developer', 20000, 'Active')
emp_2 = Employee('Jane Doe', 'Manager', 40000, 'Active')


insert_emp(emp_1)
insert_emp(emp_2)


emps = get_emp('Jane Doe')
print(emps)

update_salary(emp_2, 55000)

emps = get_emp('Jane Doe')
print(emps)

remove_emp(emp_1)


conn.close()
