# Generated by Django 4.1.7 on 2023-08-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
