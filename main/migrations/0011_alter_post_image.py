# Generated by Django 5.0.6 on 2024-07-08 17:41

import main.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=main.utils.post_directory_path),
        ),
    ]