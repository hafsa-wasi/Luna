# Generated by Django 5.0.6 on 2024-07-09 15:42

import main.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/featured-5.png', upload_to=main.utils.post_directory_path),
        ),
    ]
