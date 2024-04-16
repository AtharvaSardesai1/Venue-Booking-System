from main import *
daysList=list(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
import csv

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
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = j + 9
                if self.tt.AdjMat[daysList[i]][j].type == 0 or self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["end_time"] = j + 10
                elif self.tt.AdjMat[daysList[i]][j].subject:
                    temp["end_time"] = j + 11
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                elif self.tt.AdjMat[daysList[i]][j].subject:
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
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = j + 9
                if self.tt.AdjMat[daysList[i]][j].type == 0 or self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["end_time"] = j + 10
                elif self.tt.AdjMat[daysList[i]][j].subject:
                    temp["end_time"] = j + 11
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                elif self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
        return data


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
    


div1=SY_DIV1()
        
div2=SY_DIV2()

sub1=Subject('TOC', 4, ['Jibi', 'Soma'], 2)
sub2=Subject('MPT', 3, ['Sawant'], 2)
sub3=Subject('DSA', 2, ['Pratiksha'], 2)
sub4=Subject('VCPDE', 3, ['Seema', 'Dhere'], 2)
sub5=Subject('BFE', 3, ['Bhagyashree'], 2)
sub6=Subject('RPPOOP', 1, ['Trishna'], 2)
sub7=Subject('SA', 1, ['Kokate', 'Random'], 2)
sub8=Subject('DC', 3, ['Kshirsagar', 'Gaikwad'], 2)
lab1=Subject('MPT', 1, ['Revankar', 'Kumbhar'], 2)
lab2=Subject('DSA', 1, ['Pratiksha', 'Gaikwad'], 2)
lab3=Subject('RPPOOP', 1, ['Trishna'], 2)
lab4=Subject('SA', 1, ['M tech1', 'Mtech 2'], 2)

subjectList=[
    sub1,
    sub2,
    sub3,
    sub4,
    sub5,
    sub6,
    sub7,
    sub8
]

labList=[
    lab1,
    lab2,
    lab3,
    lab4
]
div1.RandomiseTT(subjectList,0)
div1.RandomiseTT(labList, 1)
div2.RandomiseTT(subjectList,0)
div2.RandomiseTT(labList,1)

for i in range(5):
    for j in range(7):
        if div1.classroom.tt.AdjMat[daysList[i]][j] and div2.classroom.tt.AdjMat[daysList[i]][j]:
            div1.assign_venue(203,daysList[i],j)
            div2.assign_venue(204,daysList[i],j)
        elif div1.classroom.tt.AdjMat[daysList[i]][j]:
            div1.assign_venue(203,daysList[i],j)
        elif div2.classroom.tt.AdjMat[daysList[i]][j]:
            div2.assign_venue(203,daysList[i],j)

for i in range(5):
    for j in range(7):
        k=2
        if div1.tt.AdjMat[daysList[i]][j].subject:
            div1.tt.AdjMat[daysList[i]][j].teacher=div1.tt.AdjMat[daysList[i]][j].subject.teachers[random.randint(0, len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)-1)]
            k-=1
        if div2.tt.AdjMat[daysList[i]][j].subject:
            div2.tt.AdjMat[daysList[i]][j].teacher = div2.tt.AdjMat[daysList[i]][j].subject.teachers[random.randint(0, len(div2.tt.AdjMat[daysList[i]][j].subject.teachers)-1)]

            k-=1
        if k==0 and div1.tt.AdjMat[daysList[i]][j].subject == div2.tt.AdjMat[daysList[i]][j].subject:
            if len(div2.tt.AdjMat[daysList[i]][j].subject.teachers) == 1:
                for k in div2.tt.AdjMat[daysList[i]]:
                    if k.subject != div2.tt.AdjMat[daysList[i]][j].subject:
                        k.subject, div2.tt.AdjMat[daysList[i]][j].subject=div2.tt.AdjMat[daysList[i]][j].subject, k.subject
            elif len(div2.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
                k.teacher=k.subjects[1]

print("Division 2:")
for day in div2.tt.AdjMat.keys():
    print(day)
    for i in range(0,len(div2.tt.AdjMat[day])):
        if(div2.tt.AdjMat[day][i].subject!=None and div2.tt.AdjMat[day][i].type==0):
            print(f"{i+9}-{i+10}: {div2.tt.AdjMat[day][i].subject.name}: {div2.tt.AdjMat[day][i].venue}")
        elif(div2.tt.AdjMat[day][i].subject!=None and div2.tt.AdjMat[day][i].type==1):
            print(f"{i+9}-{i+11}: {div2.tt.AdjMat[day][i].subject.name}: {div2.tt.AdjMat[day][i].venue}")
        elif(div2.tt.AdjMat[day][i].type==2):
            print(f"{i+9}-{i+10}: Lunch Break")

print("Division 1:")
for day in div1.tt.AdjMat.keys():
    print(day)
    for i in range(0,len(div1.tt.AdjMat[day])):
        if(div1.tt.AdjMat[day][i].subject!=None and div1.tt.AdjMat[day][i].type==0):
            print(f"{i+9}-{i+10}: {div1.tt.AdjMat[day][i].subject.name}: {div1.tt.AdjMat[day][i].venue}")
        elif(div1.tt.AdjMat[day][i].subject!=None and div1.tt.AdjMat[day][i].type==1):
            print(f"{i+9}-{i+11}: {div1.tt.AdjMat[day][i].subject.name}: {div1.tt.AdjMat[day][i].venue}")
        elif(div1.tt.AdjMat[day][i].type==2):
            print(f"{i+9}-{i+10}: Lunch Break")

data1=div1.generate_data()
data2=div2.generate_data()
print(data1)

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['day', 'start_time', 'end_time', 'subject', 'venue','teacher']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

write_to_csv('division1_timetable.csv', data1)
write_to_csv('division2_timetable.csv', data2)  