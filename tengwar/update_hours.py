import sqlite3
from datetime import datetime

import os
from django.core.wsgi import get_wsgi_application
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tengwar.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
application = get_wsgi_application()
django.setup()
from registration.models import Student

def main():
    ## Connects to database, selects all events from database
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT id, event_time, event_duration, student_lead_id, recursion_type FROM registration_event")
    events = cur.fetchall()

    ## Goes through every event
    for row in events:
        ## Check all event dates to make sure last event is within a week
        if checkdate(row[1], row[4]):
            ## Gets the student_id's of every student that is registered in the event
            cur.execute("SELECT student_id FROM registration_event_students_registered WHERE event_id = ?", str(row[0]))
            students_reg = []
            ## Adds the student lead into students registered first
            students_reg.append(row[3])
            for student in cur.fetchall():
                students_reg.append(student[0])
            addhours(row[2], students_reg)
    conn.close()

## Compares the event start date to the current date, determines if the event last occured within a week of the current date
def checkdate(date, recursion):
    d1 = str(date[0:10])
    d2 = str(datetime.today())[0:10]
    delta = (datetime.strptime(d2, "%Y-%m-%d") - datetime.strptime(d1, "%Y-%m-%d")).days
    ## Checks that the event has already passed
    if (0 <= delta):
        ## Checks if the event has passed within the event start date window based on recursion types:
        ## ie. if event started on jan 1, and it's jan 9 but it has weekly recursion, it returns true
        if recursion == "":
            return True
        elif recursion == "Weekly":
            if delta % 7 <= 7: return True
        elif recursion == "Bi-Weekly":
            if delta % 7 <= 14: return True
        elif recursion == "Monthly":
            if delta % 7 <= 30: return True
        return False
    
def addhours(time, students):
    time = float(formattime(time))
    ## Gets the student leaders' name
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT name FROM registration_student WHERE id = ?", (str(students[0]),))
    leader_name = cur.fetchall()[0][0]
    conn.close()
    print("To {leader}, enter attendance for all members: (1 = attended, 0 = absent)".format(leader = leader_name))
    for student in students:
        checkattendance(student, time)
    return 0

## Returns a float value which represents the hours that the students will recieve
## ex. if time is 2:30, returns 2.5
def formattime(time):
    ftime = int(time[1])
    minutes = int(time[3:5])
    if (30 <= minutes <= 50):
        ftime += 0.5
    elif (50 <= minutes):
        ftime += 1
    return ftime

def checkattendance(student, time):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT name, hours_remaining FROM registration_student WHERE id = ?", (str(student),))
    student_info = []
    for info in cur.fetchall():
        student_info.append(info[0])
        student_info.append(info[1])
    if int(input("Did {they} attend? ".format(they = student_info[0]))):
        student_info[1] = int(student_info[1]) - time
        x = Student.objects.filter(id=student)[0]
        x.hours_remaining = student_info[1]
        print(x.hours_remaining)
        x.save()

main()