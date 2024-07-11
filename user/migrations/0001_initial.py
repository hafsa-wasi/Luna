# Generated by Django 4.1.7 on 2023-08-14 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('bio', models.CharField(blank=True, max_length=120)),
                ('Email', models.EmailField(max_length=50)),
                ('Instagram', models.URLField(blank=True, max_length=150, null=True)),
                ('Linkedin', models.URLField(blank=True, max_length=150, null=True)),
                ('Twitter', models.URLField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
