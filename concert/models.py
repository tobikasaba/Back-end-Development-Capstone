from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Concert(models.Model):
    concert_name = models.CharField(max_length=255)
    duration = models.IntegerField()
    city = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)

    # __str__ controls what is displayed when a Concert object is printed or shown in the Django admin
    def __str__(self):
        # Returns the concert name so the object is human-readable instead of showing "Concert object(1)"
        return self.concert_name



class ConcertAttending(models.Model):
    class AttendingChoices(models.TextChoices):
        NOTHING = "-", _("-")
        NOT_ATTENDING = "Not Attending", _("Not Attending")
        ATTENDING = "Attending", _("Attending")

    concert = models.ForeignKey(
        Concert, null=True, on_delete=models.CASCADE, related_name="attendee"
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    attending = models.CharField(
        max_length=100,
        choices=AttendingChoices.choices,
        default=AttendingChoices.NOTHING,
    )

    class Meta:
        unique_together = ['concert', 'user']

    def __str__(self):
        return self.attending


class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    pic_url = models.CharField(max_length=1000)
    event_country = models.CharField(max_length=255)
    event_state = models.CharField(max_length=255)
    event_city = models.CharField(max_length=255)
    event_date = models.DateField(default=datetime.now)

    # Meta gives Django extra configuration for this model
    class Meta:
        # managed=False tells Django NOT to create, modify, or delete this table via migrations
        # The table is owned and managed by the external Pictures microservice, not this Django app
        managed = False

    # Returns the photo URL when the object is printed or shown in the admin
    def __str__(self):
        return self.pic_url


class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    lyrics = models.TextField()

    # Meta gives Django extra configuration for this model
    class Meta:
        # managed=False tells Django NOT to create, modify, or delete this table via migrations
        # The table is owned and managed by the external Songs microservice, not this Django app
        managed = False

    # Returns the song title when the object is printed or shown in the admin
    def __str__(self):
        return self.title
