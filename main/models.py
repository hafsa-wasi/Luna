from django.db import models
from user.models import profile
from .consts import Tags,rating
from .utils import post_directory_path
import uuid

class post(models.Model):
    id = models.UUIDField(
        primary_key=True , default=uuid.uuid4, unique=True, editable=False,)
    image = models.ImageField(upload_to=post_directory_path, null=False, default='/featured-5.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #author = models.ForeignKey(profile, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    article = models.TextField()
    author = models.ForeignKey(
        profile, on_delete=models.CASCADE, related_name='posts', null=True
    )
    category = models.CharField(max_length=24, choices=Tags , default=None)
    tag = models.CharField(max_length=24, choices=Tags , default=None)
    rating = models.CharField(max_length=20, choices=rating , default=1, null=True, blank=True)

    def __str__(self):
        return f'{self.author}\'s post'
    

class likedpost(models.Model):
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    post  = models.ForeignKey(post, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.post.heading} liked by {self.profile.user}'
    

class comments(models.Model):
    commenter_name = models.ForeignKey(profile, on_delete=models.CASCADE)
    post  = models.ForeignKey(post, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.commenter_name.user} commented on {self.post.heading} post'

