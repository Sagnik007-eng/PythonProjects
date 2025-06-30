class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def getMarks(self,sub_num):
        self.list_marks=[]
        for i in range(0,sub_num):
            marks=int(input('Enter your marks'))
            self.list_marks.append(marks)
        print(self.list_marks)
