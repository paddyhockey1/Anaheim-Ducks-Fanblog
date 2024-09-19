from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
class Meta:
    ordering = ["-created_on"]

def __str__(self):
    return f"{self.name} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

class Meta:
        ordering = ["created_on"]


def __str__(self):
    return f"{self.name} | written by {self.author}"


        # User Profile code Here

class Profile(models.Model):
        user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
        first_name = models.CharField(max_length=255, default='')
        last_name = models.CharField(max_length=255, default='')
        profile_picture = models.ImageField(upload_to='static/images', blank=True, null=True)
        bio = models.TextField(max_length=500, default='')
        favourite_Duck = models.CharField(max_length=255, default='')
        updated_on = models.DateTimeField(auto_now=True)

def __str__(self):
    return str(self.user)

