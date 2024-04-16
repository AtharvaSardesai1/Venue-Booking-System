import random

class Subject:
    def __init__(self,name,credits,teachers,year):
        self.credits=credits
        self.name=name
        self.teachers=teachers
        self.year=year


class Lecture:
    def __init__(self,type):
        self.venue=None
        self.subject=None
        self.teacher=None
        self.type=type
    def schedule(self,venue,subject):
        if (self.subject==None):
            self.subject=subject
            return 0
    def assignTeacher(self, teacher:str):
        self.teacher=teacher
        return 1

class Timetable:
    def __init__(self):
        self.AdjMat={
            'Monday':[],
            'Tuesday':[],
            'Wednesday':[],
            'Thursday':[],
            'Friday':[]
        }


    