# Generated by Django 4.1.7 on 2023-08-30 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_profile_email_remove_profile_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='profile',
        ),
        migrations.DeleteModel(
            name='signup',
        ),
    ]
