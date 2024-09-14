class Teacher:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def info(self):
        print("my name is " ,self.name , "i am a teacher of class 10th.and my id is ",self.id)


newteacher = Teacher("ahmed","hsdgc87ew")
newteacher.info()

    

class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def info(self):
        print("my name is " ,self.name , "i am a student of class 10th.and my id is ",self.id)
     
newstudent = student("bilal","hsdgc87ew")
newstudent.info()