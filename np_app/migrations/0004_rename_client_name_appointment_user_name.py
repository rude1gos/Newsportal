# Generated by Django 4.1.5 on 2023-02-21 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('np_app', '0003_remove_appointment_user_name_appointment_client_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='client_name',
            new_name='user_name',
        ),
    ]