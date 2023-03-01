# Need to find a way to format Datetime to allow timezones
# Need to find a way to input time of event, CSL hours will be added based on startime and endtime
# For models, the current isrecurring doesn't support how it is recurring, for example, some events may be recurring every week, some bi-weekly etc. Furthermore, some events, say Techo, is weekend long, so support will have to be added for events there too
# There needs to be a way to create organizations such that if the event is part of an organization, the organization will be Drop-Down in FRONTEND to eliminate margins of error
# The current version DOES NOT support days off


# This script adds events to the SQLite Database (currently via command-line)

# Necessary for the program to work, imports all libraries and sets up django
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tengwar.settings")

application = get_wsgi_application()

import django

django.setup()
from registration.models import Event
import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from datetime import datetime
from django.utils import timezone

# Will need to change organization name, students, and student contact id to pointers
# This will be done once frontend is done
organization_name = ""
event_name = ""
event_description = ""
event_date = datetime(1, 1, 1)
is_recurring = False
num_required = 0
num_registered = 0
students_registered = []
student_lead = 0
logo_image = ""
event_image = ""

recurring_type = ""
start_end_time = ""

# Will need to change so that info is recieved from frontend
# Will need to add an auto-formatting/formatting-check once frontend is done
prompts = [
    ["Organization Name:", organization_name],
    ["Event Name:", event_name],
    ["Event Description:", event_description],
    ["Event Date (USAGE: YYYY-MM-DD):", event_date],
    ["Event Start-End Times (USAGE: STARTTIME AM/PM-ENDTIME AM/PM)", start_end_time],
    ["Is it recurring (USAGE: True/False):", is_recurring],
    ["Number of students needed:", num_required],
    ["Currently Registered Students (USAGE: Id1,Id2,Id3,Id4):", num_registered],
    ["Student Head's ID Number:", student_lead],
    ["Event's Logo (USAGE: images/logo/event_name.jpg):", logo_image],
    [
        "Image of the Event (USAGE: images/event_image//event_nameevent.jpg):",
        event_image,
    ],
]

# Will need to change when frontend is done
for i in range(len(prompts)):
    print(prompts[i][0])
    prompts[i][1] = input()

is_recurring = prompts[4][1]
print(is_recurring)

if is_recurring:
    print("Recursion Type:")
    print("Types: Weekly, Bi-Weekly, Monthly, Other")
    recurring_type = input()
    if recurring_type == "Other":
        print("Specify (USAGE EX: Monday and Wednesday, Weekly):")
        recurring_type = input()
students = []
students.append(prompts[6][1].split(","))

event = Event(
    organization_name=prompts[0][1],
    event_name=prompts[1][1],
    event_description=prompts[2][1],
    event_date=prompts[3][1],
    event_times=prompts[4][1],
    is_recurring=prompts[5][1],
    num_required=prompts[6][1],
    num_registered=len(prompts[6][1].split(",")),
    student_lead=prompts[8][1],
    logo_upload=prompts[9][1],
    event_pic_upload=prompts[10][1],
    recursion_type=recurring_type,
)
event.save()
event.students_registered.set(students)
