# Generated by Django 4.0.2 on 2022-02-02 09:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_profile',
            new_name='UserProfile',
        ),
    ]
