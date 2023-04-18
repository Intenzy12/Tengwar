from datetime import datetime

import os
from django.core.wsgi import get_wsgi_application
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tengwar.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
application = get_wsgi_application()
django.setup()
from registration.models import Student, Event

def main():
    # Gets all events from database
    events = Event.objects.all()
    for event in events:
        ## Check all event dates to make sure last event is within a week"
        if checkdate(event.event_time, event.recursion_type):
            x = Event.objects.filter(id=event.id)[0].students_registered.all()
            ## Honestly, lines related to students_reg exist because I don't know how to store each student
            ## plus the leader in one variable any other way and they must be in an array, so I combined x with student leader
            ## that's the use of students_reg -- sorry
            students_reg = []
            ## Adds the student lead into students registered first
            students_reg.append(event.student_lead)
            for student in x:
                students_reg.append(student)
            addhours(event.event_duration, students_reg)

## Compares the event start date to the current date, determines if the event last occured within a week of the current date
def checkdate(date, recursion):
    d1 = str(date)[0:10]
    d2 = str(datetime.today())[0:10]
    delta = (datetime.strptime(d2, "%Y-%m-%d") - datetime.strptime(d1, "%Y-%m-%d")).days
    ## Checks that the event has already passed
    if (0 <= delta):
        ## Checks if the event has passed within the event start date window based on recursion types:
        ## ie. if event started on jan 1, and it's jan 9 but it has weekly recursion, it returns true
        if recursion == "": return True
        elif recursion == "Weekly" and delta % 7 <= 7: return True
        elif recursion == "Bi-Weekly" and delta % 7 <= 14: return True
        elif recursion == "Monthly" and delta % 7 <= 30: return True
        return False
    
def addhours(time, students):
    time = float(formattime(time))
    ## Gets the student leaders' name
    x = Student.objects.filter(id = students[0].id)[0]
    print("To {leader}, enter attendance for all members: (1 = attended, 0 = absent)".format(leader = x.name))
    for student in students:
        checkattendance(student, time)
    return 0

## Returns a float value which represents the hours that the students will recieve
## ex. if time is 2:30, returns 2.5
def formattime(time):
    ftime = int(str(time)[1])
    minutes = int(str(time)[3:5])
    if (30 <= minutes <= 50):
        ftime += 0.5
    elif (50 <= minutes):
        ftime += 1
    return ftime

## Asks whether or not each student attended, if so, hours are added
def checkattendance(student, time):
    x = Student.objects.filter(id=student.id)[0]
    if int(input("Did {they} attend? ".format(they = x.name))):
        x.hours_remaining = x.hours_remaining - time
        x.save()
main()