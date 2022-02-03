from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import *


def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email !='':
        user.username = user.email
    print('email set as username')
pre_save.connect(updateUser, sender=User)

def sendMail(sender, instance, created, **kwargs,):
    if created:
        print(instance)
        subject = 'Welcome to Idea Thinker'
        html_message = render_to_string('base/welcome_email.html', 
        {'fullName': instance.last_name +' '+ instance.first_name, 'email':instance.email })
        plain_message = strip_tags(html_message) 
        from_email = 'abdulahiopeyemiq1@gmail.com'
        to= instance.email

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        print('message sent') 
post_save.connect(sendMail, sender=User)
