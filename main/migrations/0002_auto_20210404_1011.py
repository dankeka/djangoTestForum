# Generated by Django 3.1.7 on 2021-04-04 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeruserform',
            name='profile_ptr',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='RegisterUserForm',
        ),
    ]