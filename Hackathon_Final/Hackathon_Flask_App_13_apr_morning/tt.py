daysList=list(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
import csv
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

class Classroom:
    def __init__(self):
        self.tt=Timetable()
        for day in self.tt.AdjMat.keys():
            for i in range (7):
                self.tt.AdjMat[day].append(0)
    def scheduleAt(self, day, time):
        self.tt.AdjMat[day][time]=1
    def getNextFree(self, day, time):
        daysList=list(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        i=daysList.index(day)
        availableTime=time
        for k in range(i, 5):
            while self.tt[daysList[i]][availableTime] == 0:
                return (day, availableTime)
            
        return (-1, -1)



class SY_DIV1:
    def __init__(self):
        self.tt=Timetable()
        self.classroom=Classroom()
        for day in self.tt.AdjMat.keys():
            self.tt.AdjMat[day].append(Lecture(0))  # 0:lecture   1:Lab   2:Break
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(1))
            self.tt.AdjMat[day].append(Lecture(2))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
    
    def check(self,subject,day):
        for i in range(0,len(self.tt.AdjMat[day])):
            if subject==self.tt.AdjMat[day][i].subject:
                return 0
        return 1

    def assign_venue(self,venue,day,time):
        self.tt.AdjMat[day][time].venue=venue
    
    def RandomiseTT(self, subjectList, type):
        for subject in subjectList:
            i=0
            while i<subject.credits:
                day=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                timeSlot=random.randint(0, 6)
                if self.tt.AdjMat[day][timeSlot].type != type:
                    continue
                if self.check(subject,day):
                    res=self.tt.AdjMat[day][timeSlot].schedule(None,subject)
                    if self.tt.AdjMat[day][timeSlot].type==0 :
                        self.classroom.scheduleAt(day, timeSlot)
                    if res==0:
                        i+=1
    
    def generate_data(self):
        data = []
        for i in range(5):
            startTime=9
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = startTime
                if self.tt.AdjMat[daysList[i]][j].type == 0 or self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["end_time"] = startTime+1
                    startTime += 1
                elif self.tt.AdjMat[daysList[i]][j].type == 1:
                    temp["end_time"] = startTime + 2
                    startTime += 2
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                if self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
        return data

class SY_DIV2:
    def __init__(self):
        self.tt=Timetable()
        self.classroom=Classroom()
        for day in self.tt.AdjMat.keys():
            self.tt.AdjMat[day].append(Lecture(1))  # 0:lecture   1:Lab   2:Break
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(2))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(3))
    
    def check(self,subject,day):
        for i in range(0,len(self.tt.AdjMat[day])):
            if subject==self.tt.AdjMat[day][i].subject:
                return 0
        return 1
    
    def assign_venue(self,venue,day,time):
        self.tt.AdjMat[day][time].venue=venue
    
    def RandomiseTT(self, subjectList, type):
        for subject in subjectList:
            i=0
            while i<subject.credits:
                day=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                timeSlot=random.randint(0, 6)
                if self.tt.AdjMat[day][timeSlot].type != type:
                    continue
                if self.check(subject,day):
                    res=self.tt.AdjMat[day][timeSlot].schedule(None,subject)
                    if self.tt.AdjMat[day][timeSlot].type==0 :
                        self.classroom.scheduleAt(day, timeSlot)
                    if res==0:
                        i+=1
    
    def generate_data(self):
        data = []
        for i in range(5):
            startTime=9
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = startTime
                if self.tt.AdjMat[daysList[i]][j].type != 1:
                    temp["end_time"] = startTime + 1
                    startTime += 1
                elif self.tt.AdjMat[daysList[i]][j].type == 1:
                    temp["end_time"] = startTime + 2
                    startTime += 2
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                if self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
        return data

class TY_DIV1:
    def __init__(self):
        self.tt=Timetable()
        self.classroom=Classroom()
        for day in self.tt.AdjMat.keys():
            self.tt.AdjMat[day].append(Lecture(0))  # 0:lecture   1:Lab   2:Break 3:honors 4:electives
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(4))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(2))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(1))
            self.tt.AdjMat[day].append(Lecture(3))
    
    def check(self,subject,day):
        for i in range(0,len(self.tt.AdjMat[day])):
            if subject==self.tt.AdjMat[day][i].subject:
                return 0
        return 1

    def assign_venue(self,venue,day,time):
        if not self.tt.AdjMat[day][time].type:
            self.tt.AdjMat[day][time].venue=venue
    
    def RandomiseTT(self, subjectList, type):
        for subject in subjectList:
            i=0
            while i<subject.credits:
                day=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                timeSlot=random.randint(0, 6)
                if self.tt.AdjMat[day][timeSlot].type != type:
                    continue
                if self.check(subject,day):
                    res=self.tt.AdjMat[day][timeSlot].schedule(None,subject)
                    if self.tt.AdjMat[day][timeSlot].type==0 :
                        self.classroom.scheduleAt(day, timeSlot)
                    if res==0:
                        i+=1
    
    def generate_data(self):
        data = []
        for i in range(5):
            startTime=9
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = startTime
                if self.tt.AdjMat[daysList[i]][j].type != 1:
                    temp["end_time"] = startTime + 1
                    startTime += 1
                elif self.tt.AdjMat[daysList[i]][j].type == 1:
                    temp["end_time"] = startTime + 2
                    startTime += 2
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                if self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
        return data

class TY_DIV2:
    def __init__(self):
        self.tt=Timetable()
        self.classroom=Classroom()
        for day in self.tt.AdjMat.keys():
            self.tt.AdjMat[day].append(Lecture(0))  # 0:lecture   1:Lab   2:Break  3:honors 4: electives
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(4))
            self.tt.AdjMat[day].append(Lecture(2))
            self.tt.AdjMat[day].append(Lecture(1))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(3))

    
    def check(self,subject,day):
        for i in range(0,len(self.tt.AdjMat[day])):
            if subject==self.tt.AdjMat[day][i].subject:
                return 0
        return 1

    def assign_venue(self,venue,day,time):
        if not self.tt.AdjMat[day][time].type:
            self.tt.AdjMat[day][time].venue=venue
    
    def RandomiseTT(self, subjectList, type):
        for subject in subjectList:
            i=0
            while i<subject.credits:
                day=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                timeSlot=random.randint(0, 6)
                if self.tt.AdjMat[day][timeSlot].type != type:
                    continue
                if self.check(subject,day):
                    res=self.tt.AdjMat[day][timeSlot].schedule(None,subject)
                    if self.tt.AdjMat[day][timeSlot].type==0 :
                        self.classroom.scheduleAt(day, timeSlot)
                    if res==0:
                        i+=1
    
    def generate_data(self):
        data = []
        for i in range(5):
            startTime=9
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = startTime
                if self.tt.AdjMat[daysList[i]][j].type != 1:
                    temp["end_time"] = startTime + 1
                    startTime += 1
                elif self.tt.AdjMat[daysList[i]][j].type == 1:
                    temp["end_time"] = startTime + 2
                    startTime += 2
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                if self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
        return data

sy_div1=SY_DIV1()    
sy_div2=SY_DIV2()

ty_div1=TY_DIV1()
ty_div2=TY_DIV2()

sy_sub1=Subject('TOC', 4, ['Jibi', 'Soma'], 2)
sy_sub2=Subject('MPT', 3, ['Sawant'], 2)
sy_sub3=Subject('DSA', 2, ['Pratiksha'], 2)
sy_sub4=Subject('VCPDE', 3, ['Seema', 'Dhere'], 2)
sy_sub5=Subject('BFE', 3, ['Bhagyashree'], 2)
sy_sub6=Subject('RPPOOP', 1, ['Trishna'], 2)
sy_sub7=Subject('SA', 1, ['Kokate', 'Random'], 2)
sy_sub8=Subject('DC', 3, ['Kshirsagar', 'Gaikwad'], 2)
sy_lab1=Subject('MPT', 1, ['Revankar', 'Kumbhar'], 2)
sy_lab2=Subject('DSA', 1, ['Pratiksha', 'Gaikwad'], 2)
sy_lab3=Subject('RPPOOP', 1, ['Trishna'], 2)
sy_lab4=Subject('SA', 1, ['M tech1', 'Mtech 2'], 2)

ty_sub1=Subject('SE-2', 3, ['Tanuja', 'Pradeep'], 3)
ty_sub2=Subject('DS', 3, ['Archana'], 3)
ty_sub3=Subject('DAA', 4, ['Aparna'], 3)
ty_sub4=Subject('OS', 3, ['Abhijeet'], 3)
ty_lab1=Subject('SE-2', 1, ['Tanuja', 'Jibi'], 3)
ty_lab2=Subject('OS', 1, ['Abhijeet', 'Anish', 'Amit'], 3)
ty_lab3=Subject('DS', 1, ['Khushal', 'Yashodhara', 'Archana'], 3)
ty_lab4=Subject('DEC', 1, ['RANDOM1', 'RANDOM2', 'RANDOM3'], 3)
ty_sub5=Subject('DEC',3, ['Deepika', 'Shraddha', 'Vijay'], 3)



sy_subjectList=[sy_sub1, sy_sub2, sy_sub3, sy_sub4, sy_sub5, sy_sub6, sy_sub7, sy_sub8]
sy_labList=[sy_lab1,sy_lab2,sy_lab3,sy_lab4]

ty_subjectList=[ty_sub1, ty_sub2, ty_sub3, ty_sub4]
ty_labList=[ty_lab1,ty_lab2,ty_lab3,ty_lab4]

ty_electiveList=[ty_sub5]

sy_div1.RandomiseTT(sy_subjectList,0)
sy_div1.RandomiseTT(sy_labList, 1)
sy_div2.RandomiseTT(sy_subjectList,0)
sy_div2.RandomiseTT(sy_labList,1)

ty_div1.RandomiseTT(ty_subjectList,0)
ty_div1.RandomiseTT(ty_labList, 1)
ty_div2.RandomiseTT(ty_subjectList,0)
ty_div2.RandomiseTT(ty_labList,1)
ty_div1.RandomiseTT(ty_electiveList, 4)
ty_div2.RandomiseTT(ty_electiveList, 4)

def SY_COMP(div1,div2):
    for i in range(5):
        for j in range(7):
            if div1.classroom.tt.AdjMat[daysList[i]][j] and div2.classroom.tt.AdjMat[daysList[i]][j]:
                div1.assign_venue(203,daysList[i],j)
                div2.assign_venue(201,daysList[i],j)
            elif div1.classroom.tt.AdjMat[daysList[i]][j]:
                div1.assign_venue(203,daysList[i],j)
            elif div2.classroom.tt.AdjMat[daysList[i]][j]:
                div2.assign_venue(203,daysList[i],j)

    for i in range(5):
        for j in range(7):
            if div1.tt.AdjMat[daysList[i]][j].subject and div2.tt.AdjMat[daysList[i]][j].subject and div1.tt.AdjMat[daysList[i]][j].subject.name==div2.tt.AdjMat[daysList[i]][j].subject.name:
                if len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)==1:
                    for m in div2.tt.AdjMat[daysList[i]]:
                        if m.subject != div2.tt.AdjMat[daysList[i]][j].subject:
                            m.subject, div2.tt.AdjMat[daysList[i]][j].subject=div2.tt.AdjMat[daysList[i]][j].subject, m.subject
                else:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[1])
            else:
                if div1.tt.AdjMat[daysList[i]][j].subject and len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
                    if div1.tt.AdjMat[daysList[i]][j].subject:
                        div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    if div2.tt.AdjMat[daysList[i]][j].subject:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                else:
                    if div1.tt.AdjMat[daysList[i]][j].subject:
                        div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    if div2.tt.AdjMat[daysList[i]][j].subject:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[0])

def TY_COMP(div1,div2):
    for i in range(5):
        for j in range(7):
            if j==2:
                if sy_div2.tt.AdjMat[daysList[i]][j].venue==201:
                        div1.tt.AdjMat[daysList[i]][j].venue=204
                        div2.tt.AdjMat[daysList[i]][j].venue=204
                else:
                        div1.tt.AdjMat[daysList[i]][j].venue=201
                        div2.tt.AdjMat[daysList[i]][j].venue=201
                continue
            if div1.classroom.tt.AdjMat[daysList[i]][j] and div2.classroom.tt.AdjMat[daysList[i]][j]:
                div1.assign_venue(202,daysList[i],j)
                if sy_div2.classroom.tt.AdjMat[daysList[i]][j]==0 or sy_div2.tt.AdjMat[daysList[i]][j].venue==203:
                    div2.assign_venue(201,daysList[i],j)
                else:
                    div2.assign_venue(204,daysList[i],j)
            elif div1.classroom.tt.AdjMat[daysList[i]][j]:
                div1.assign_venue(202,daysList[i],j)
            elif div2.classroom.tt.AdjMat[daysList[i]][j]:
                div2.assign_venue(202,daysList[i],j)

    for i in range(5):
        for j in range(7):
            if div1.tt.AdjMat[daysList[i]][j].subject and div2.tt.AdjMat[daysList[i]][j].subject and div1.tt.AdjMat[daysList[i]][j].subject.name==div2.tt.AdjMat[daysList[i]][j].subject.name:
                if len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)==1:
                    for m in div2.tt.AdjMat[daysList[i]]:
                        if m.subject != div2.tt.AdjMat[daysList[i]][j].subject:
                            m.subject, div2.tt.AdjMat[daysList[i]][j].subject=div2.tt.AdjMat[daysList[i]][j].subject, m.subject
                else:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[1])
            else:
                if div1.tt.AdjMat[daysList[i]][j].subject and len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
                    if div1.tt.AdjMat[daysList[i]][j].subject:
                        div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    if div2.tt.AdjMat[daysList[i]][j].subject:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                else:
                    if div1.tt.AdjMat[daysList[i]][j].subject:
                        div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    if div2.tt.AdjMat[daysList[i]][j].subject:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[0])

            # k=2
            # if div1.tt.AdjMat[daysList[i]][j].subject:
            #     if div1.tt.AdjMat[daysList[i]][j].teacher==None:
            #         div1.tt.AdjMat[daysList[i]][j].teacher=div1.tt.AdjMat[daysList[i]][j].subject.teachers[random.randint(0, len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)-1)]
            #     k-=1
            # if div2.tt.AdjMat[daysList[i]][j].subject:
            #     if div1.tt.AdjMat[daysList[i]][j].teacher==None:
            #         div2.tt.AdjMat[daysList[i]][j].teacher = div2.tt.AdjMat[daysList[i]][j].subject.teachers[random.randint(0, len(div2.tt.AdjMat[daysList[i]][j].subject.teachers)-1)]
            #     k-=1
            # if k==0 and div1.tt.AdjMat[daysList[i]][j].subject == div2.tt.AdjMat[daysList[i]][j].subject:
            #     if len(div2.tt.AdjMat[daysList[i]][j].subject.teachers) == 1:
            #         for m in div2.tt.AdjMat[daysList[i]]:
            #             if m.subject != div2.tt.AdjMat[daysList[i]][j].subject:
            #                 m.subject, div2.tt.AdjMat[daysList[i]][j].subject=div2.tt.AdjMat[daysList[i]][j].subject, m.subject
            #     elif len(div2.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
            #         div2.tt.AdjMat[daysList[i]][j].teacher=div2.tt.AdjMat[daysList[i]][j].subject.teachers[1]
    for i in range(5):
        if div1.tt.AdjMat[daysList[i]][2].subject:
            div2.tt.AdjMat[daysList[i]][2].subject=div1.tt.AdjMat[daysList[i]][2].subject
            div2.tt.AdjMat[daysList[i]][2].venue=div1.tt.AdjMat[daysList[i]][2].venue

SY_COMP(sy_div1,sy_div2)
TY_COMP(ty_div1,ty_div2)

sy_data1=sy_div1.generate_data()
sy_data2=sy_div2.generate_data()

ty_data1=ty_div1.generate_data()
ty_data2=ty_div2.generate_data()

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['day', 'start_time', 'end_time', 'subject', 'venue','teacher']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

write_to_csv('sy_division1_timetable.csv', sy_data1)
write_to_csv('sy_division2_timetable.csv', sy_data2)  

write_to_csv('ty_division1_timetable.csv', ty_data1)
write_to_csv('ty_division2_timetable.csv', ty_data2)  