from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    to_field = models.CharField(max_length=50)
    do_field = models.CharField(max_length=75)
    when = models.CharField(max_length=50)
    support_link = models.CharField(max_length=1000, null=False)
    summary = models.TextField(max_length=400)
    contributor = models.CharField(max_length=50)
    likes = models.ManyToManyField('auth.User', related_name='likes')
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.to_field

    @property
    def total_likes(self):
        """
        Likes for the post
        :return: Integer: Subscribes for the post
        """
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    entry = models.CharField(max_length=100, default='xxx')
    post = models.ForeignKey(Post)
    created_date = models.DateTimeField(
            default=timezone.now)
