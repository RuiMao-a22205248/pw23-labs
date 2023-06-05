from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_link = models.URLField()
    pythonanywhere_link = models.URLField()

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    account = models.OneToOneField(Account, null=False, on_delete=models.CASCADE)
    areas = models.ManyToManyField('Area', related_name='blogs')

    def __str__(self):
        return f"Blog of {self.account.user.username}"


class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    areas = models.ManyToManyField(Area, related_name='areas')

    def __str__(self):
        return self.name


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.title


class Like(models.Model):
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"Post {self.post.title} has {self.likes} likes"
