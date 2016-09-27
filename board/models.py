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

    def total_follows(self, frequency):
        """
        Followers for the post
        :return: Integer: Subscribes for the post
        """
        return self.follow_set.filter(frequency=frequency).count()

    @property
    def total_daily(self):
        """
        Followers for the post
        :return: Integer: Subscribes for the post
        """
        return self.total_follows(frequency=Follow.DAILY)

    @property
    def total_weekly(self):
        """
        Followers for the post
        :return: Integer: Subscribes for the post
        """
        return self.total_follows(frequency=Follow.WEEKLY)

    @property
    def total_monthly(self):
        """
        Followers for the post
        :return: Integer: Subscribes for the post
        """
        return self.total_follows(frequency=Follow.MONTHLY)

    @property
    def total_all_follows(self):
        """
        Likes for the post
        :return: Integer: Subscribes for the post
        """
        return self.follow_set.count()


class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    entry = models.CharField(max_length=100, default='xxx')
    post = models.ForeignKey(Post)
    created_date = models.DateTimeField(
            default=timezone.now)


class Follow(models.Model):
    user = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post)
    DAILY = 1
    WEEKLY = 3
    MONTHLY = 6
    FREQUENCY_CHOICES = (
        (DAILY, 'daily'),
        (WEEKLY, 'weekly'),
        (MONTHLY, 'monthly'),
    )
    frequency = models.PositiveSmallIntegerField(
        choices=FREQUENCY_CHOICES,
    )

    class Meta:
        unique_together = ("user", "post")
