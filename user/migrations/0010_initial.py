# Generated by Django 4.1.7 on 2023-08-30 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0009_delete_profile_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(4)])),
                ('repassword', models.CharField(max_length=20)),
            ],
        ),
    ]
