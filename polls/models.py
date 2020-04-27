from django.db import models
import datetime
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=128)
    # will import from BaseUser
    # email, profile_image, password, streak will be added later

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Set(models.Model):
    name = models.CharField(max_length=200, unique=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.name}"

    @property
    def contents(self):
        return self.content_sets.all()


class Content(models.Model):
    text = models.TextField()
    set = models.ForeignKey(
        Set, related_name="content_sets", on_delete=models.CASCADE)

    def __str__(self):
        return f"Content: {self.id}"


class UserSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


class BookMark(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content}"


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
