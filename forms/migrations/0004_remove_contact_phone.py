# Generated by Django 4.1.1 on 2023-04-23 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_contact_message_contact_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
