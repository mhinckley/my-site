from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    to_field = models.CharField(max_length=50, default='xxx')
    do_field = models.CharField(max_length=75, default='xxx')
    when = models.CharField(max_length=50, default='sss')
    content_type = models.CharField(max_length=50, blank=True, default='some string')
    support_link = models.CharField(max_length=1000, null=False, default='xxx')
    summary = models.TextField(max_length=1000, default='xxx')
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.to_field


