from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='author_avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    content = RichTextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category, related_name='posts')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    is_published = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    approved = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'