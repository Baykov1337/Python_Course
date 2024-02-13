class TeamMember:
    def __init__(self,name, userit):
         self.name = name
         self.userit = userit
    

class Worker:
    def __init__(self,pay,jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle


class TeamLeader(TeamMember,Worker):
    def __init__(self,name, userit,pay, jobtitle, exp):
        TeamMember.__init__(self,name,userit) 
        Worker.__init__(self,pay,jobtitle)
        self.exp = exp
        print (f"The name:{self.name}, Salary:{self.pay}, JobTitle: {self.jobtitle} Experience year : {self.exp}")
TeamLeader ("Ben", 1, 5,"TL", 8 )

