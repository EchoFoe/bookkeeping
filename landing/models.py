from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email = models.EmailField(max_length=256)
    name = models.CharField(max_length=128, default=None)
    subject = models.CharField(max_length=128, default=None)
    message = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s" "%s" % (self.email, self.name)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Followers'