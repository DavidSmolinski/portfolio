from django.db import models
from django.db.models import PositiveSmallIntegerField


class Rating(models.Model):
    """Somerville Happiness Survey data"""
    # ip = models.GenericIPAddressField()
    ip = models.CharField(max_length=16)  # ip address

    HAPPY_CHOICES = [(0, 'no'), (1, 'yes')]
    RATING_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

    happy = PositiveSmallIntegerField(choices=HAPPY_CHOICES)
    info = PositiveSmallIntegerField(choices=RATING_CHOICES)
    housing = PositiveSmallIntegerField(choices=RATING_CHOICES)
    schools = PositiveSmallIntegerField(choices=RATING_CHOICES)
    police = PositiveSmallIntegerField(choices=RATING_CHOICES)
    streets = PositiveSmallIntegerField(choices=RATING_CHOICES)
    events = PositiveSmallIntegerField(choices=RATING_CHOICES)
