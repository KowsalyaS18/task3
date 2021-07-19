class Student():
    def __init__(self,Studentid,Studentname):
        self.Studentid=Studentid
        self.Studentname=Studentname
        
Stu=Student("s101","kowsi")
print(Stu.Studentid)
print(Stu.Studentname)
setattr(Stu,'Studentclass','VI')
print(getattr(Stu,'Studentclass'))
        
   
    
