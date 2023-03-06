import os
from django.core.wsgi import get_wsgi_application
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tengwar.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
application = get_wsgi_application()
django.setup()

from registration.models import Teacher


with open("./teachers.csv", 'r') as data:
    teachers = data.readlines()[1:]
    
for teacher in teachers:
    temp = teacher.replace('"', '').split(",")
    Teacher(name=f"{temp[0]} {temp[1]}", email=f"{temp[0].lower()}.{temp[1].lower()}@asfm.edu.mx", gender=temp[2]).save()