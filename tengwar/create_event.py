# DO NOT DELETE
import os
from django.core.wsgi import get_wsgi_application
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tengwar.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
application = get_wsgi_application()
django.setup()



from registration.models import Event, Student, Teacher
from datetime import datetime, time
from django.utils import timezone
import pytz

data = {}
data_keys = [
    "organization name",
    "event name",
    "event description",
    "event date",
    "event start time",
    "event end time",
    "is recurring",
    "num required",
    "students registered",
    "student lead",
    "advisor",
    "event logo",
    "event image",
]

prompts = [
    "Organization Name:\n",
    "Event Name:\n",
    "Event Description:\n",
    "Event Date (USAGE: YYYY/MM/DD):\n",
    "Event Start Time (USAGE: hh:mm):\n",
    "Event End Time (USAGE: hh:mm):\n",
    "Is it recurring (USAGE: Yes/No):\n",
    "Number of students required:\n",
    "Currently Registered Students (USAGE: Id1, Id2, Id3, ...):\n",
    "Student Head's Id Number:\n",
    "Teacher Advisor's Email:\n",
    "Event's Logo (USAGE: EVENTNAME.jpg):\n",
    "Image of the Event (USAGE: EVENTNAME.jpg):\n",
]

# Take input for all the required options
for prompt, key in zip(prompts, data_keys):
    data[key] = input(prompt)
    
# Prompt more options if there is recursion in event
if data["is recurring"].title() == "Yes":
    data["is recurring"] = True
else:
    data["is recurring"] = False

recursion_type = ""
if data["is recurring"]:
    print("Recursion Type: ")
    recursion_type = input("Types: Weekly, Bi-Weekly, Monthly, Other \n")
    
    if recursion_type == "Other":
        recursion_type = input("Specify (USAGE EX: Monday and Wednesday, Weekly):\n")

data["recursion type"] = recursion_type

# change start and end time to datetime obejct
data["event start time"] = datetime.strptime(f"{data['event date']} {data['event start time']}", "%Y/%m/%d %H:%M").replace(tzinfo=pytz.timezone("America/Mexico_City"))
data["event end time"] = datetime.strptime(f"{data['event date']} {data['event end time']}", "%Y/%m/%d %H:%M").replace(tzinfo=pytz.timezone("America/Mexico_City"))
timezone.localtime()

# declare the event object
x = Event(
    organization_name=data["organization name"],
    event_name=data["event name"],
    event_description=data["event description"],
    event_time=data["event start time"],
    event_duration=(datetime.min + (data["event end time"] - data["event start time"])).time(),
    event_end_time=data["event end time"].time(),
    is_recurring=data["is recurring"],
    num_required=int(data["num required"]),
    num_registered=len(data["students registered"].split(", ")),
    student_lead=Student.objects.filter(student_id=int(data["student lead"]))[0],
    advisor=Teacher.objects.filter(email=data["advisor"])[0],
    logo_upload=data["event logo"],
    event_pic_upload=data["event image"],
    recursion_type=data["recursion type"]
)

x.save()