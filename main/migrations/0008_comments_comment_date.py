# Generated by Django 4.1.7 on 2023-10-10 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
