# Generated by Django 4.1.7 on 2023-08-18 12:42

from django.db import migrations, models
import user.utils


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=user.utils.user_directory_path),
        ),
    ]
