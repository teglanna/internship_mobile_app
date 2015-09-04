from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.auth.models import User

class DateHelper(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class CheckIn(DateHelper):
    user = models.ForeignKey(User)
    location = models.PointField(null=False, blank=False)

    def __unicode__(self):
        x = self.location.get_x()
        y = self.location.get_y()
        return "at (%f, %f) for %s" % (x, y, self.user)


class StuffManager(models.GeoManager):

    """
    :location: reference location
    :proximity: distance radius limit
    """
    def sort_by_distance(self, location=Point(1.232433, 1.2323232), proximity=settings.PROXIMITY_DEFAULT):
        return self.get_queryset().filter(location__distance_lte=(location, D(m=proximity))).distance(location).order_by('distance')


class Stuff(DateHelper):
    user = models.ForeignKey(User)
    location = models.PointField(null=False, blank=False)
    description = models.CharField(max_length=500)
    pickup = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    price = models.IntegerField()
    main_img = models.OneToOneField("swipebuy_app.Image", blank=True, null=True, related_name='main_image')
    active = models.BooleanField(default=True)
    buy_time = models.DateTimeField(null=True, blank=True)

    objects = StuffManager()

    def __unicode__(self):
        return "%s (user: %s) [active: %r] for %d" % (self.description, self.user, self.active, self.price)


class Image(DateHelper):
    stuff = models.ForeignKey(Stuff)
    image = models.ImageField()

    def __unicode__(self):
        return "%s for %s" % (self.image.name, self.stuff)


class Message(DateHelper):
    stuff = models.ForeignKey(Stuff)
    author = models.ForeignKey(User)
    text = models.TextField(max_length=500)
    recipient = models.ForeignKey(User, related_name='message_recipients', blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "[from: %s to: %s] %s" % (self.author, self.recipient, self.text)


class SwipeAction(DateHelper):
    SWIPING, MAKE_BID, BUY= 0, 1, 2
    ACTION_CHOICES = (
        (SWIPING, 'swiping'),
        (MAKE_BID, 'make bid'),
        (BUY, 'buy'),
    )
    user = models.ForeignKey(User)
    stuff = models.ForeignKey(Stuff)
    action = models.IntegerField(choices=ACTION_CHOICES)

    def __unicode__(self):
        return "action: %s for %s for %s" % (self.ACTION_CHOICES[self.action][1], self.stuff, self.user)
