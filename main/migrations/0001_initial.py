# Generated by Django 4.1.7 on 2023-09-03 18:31

from django.db import migrations, models
import django.db.models.deletion
import user.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0013_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(default='main/images/images.jpg', null=True, upload_to=user.utils.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('article', models.TextField()),
                ('category', models.CharField(choices=[('travel', 'Travel'), ('culture', 'Culture'), ('lifestyle', 'Lifestyle'), ('fashion', 'Fashion'), ('food', 'Food'), ('space', 'Space'), ('animal', 'Animal'), ('minimal', 'Minimal'), ('interior', 'Interior'), ('plant', 'Plant'), ('nature', 'Nature'), ('business', 'Business'), ('design', 'Design'), ('movie', 'Movie'), ('sport', 'Sport')], default=None, max_length=24)),
                ('tag', models.CharField(choices=[('travel', 'Travel'), ('culture', 'Culture'), ('lifestyle', 'Lifestyle'), ('fashion', 'Fashion'), ('food', 'Food'), ('space', 'Space'), ('animal', 'Animal'), ('minimal', 'Minimal'), ('interior', 'Interior'), ('plant', 'Plant'), ('nature', 'Nature'), ('business', 'Business'), ('design', 'Design'), ('movie', 'Movie'), ('sport', 'Sport')], default=None, max_length=24)),
                ('rating', models.CharField(choices=[('travel', 'Travel'), ('culture', 'Culture'), ('lifestyle', 'Lifestyle'), ('fashion', 'Fashion'), ('food', 'Food'), ('space', 'Space'), ('animal', 'Animal'), ('minimal', 'Minimal'), ('interior', 'Interior'), ('plant', 'Plant'), ('nature', 'Nature'), ('business', 'Business'), ('design', 'Design'), ('movie', 'Movie'), ('sport', 'Sport')], default=None, max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='user.profile')),
            ],
        ),
    ]