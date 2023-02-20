# TO DO:
# Need to make sure that when updating database ONLY the people whose hours have changed are updated
# Need to make sure that when updating database NO extra people are added
# Need to find a way to automatically update database whenever hours are updated

# Necessary for the program to work, imports all libraries and sets up django
import django
django.setup()
from registration.models import Student
import csv
import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Declares array where data from csv file is stored
data = []

# Reads and imports csv file into data
# CSV file MUST be named 'ftable.csv'
with open('./ftable.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in file:
        data.append(row.split(","))

# Adds data to students by creating 'Student' object and saving it to the database
# CHANGE NECESSARY for updating database
for i in range(len(data)):
    student = Student(name = data[i][1], email= data[i][3], student_id = data[i][0], grad_year = data[i][3][:2], hours_remaining = data[i][2])
    student.save()
