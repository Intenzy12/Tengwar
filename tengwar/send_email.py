import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tengwar.settings')
application = get_wsgi_application()

import django
django.setup()

from registration.models import Student, Event


from email.message import EmailMessage
import ssl
import smtplib
from django.utils import timezone

class Email():
    def __self__(self, text):
        self.body = text

    def send_email(self):
        sender = "cce@asfm.mx"
        password = os.environ.get("EMAIL_PASSWORD")
        recievers = []
        events = Event.objects.filter(event_time__lte=timezone.now())


        for event in events:
            for student in event.students_registered.all():
                student.hours_remaining -= event.hours_rewarded
                student.save()
                recievers.append(student.email.strip())

            
            message = (
                f'From: {sender}\n'
                f'To: {recievers}\n'
                f'Text: HELLO MY NAME IS '
            )
            recievers = ", ".join(recievers)

            em = EmailMessage()

            em['From'] = sender
            em['To'] = recievers
            em['Subject'] = f"{event.organization_name}: {event.event_name} activity report"
            em.set_content(message)

            # ssl for security
            context = ssl.create_default_context()
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(sender, password)
                smtp.sendmail(sender, recievers, em.as_string())
            
            recievers = []