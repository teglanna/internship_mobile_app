# from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User

action_choices = (
    (1, 'swiping'),
    (2, 'make_bid'),
    (3, 'buy'),
)


class DateHelper(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class CheckIn(DateHelper):
    user = models.ForeignKey(User)
    location = models.PointField(null=False, blank=False)

    def __unicode__(self):
        return self.location, self.user


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

    def __unicode__(self):
        return self.description, self.user, self.active, self.price


class Image(DateHelper):
    stuff = models.ForeignKey(Stuff)
    image = models.ImageField()

    def __unicode__(self):
        return self.image.url


class Message(DateHelper):
    stuff = models.ForeignKey(Stuff)
    author = models.ForeignKey(User)
    text = models.TextField(max_length=500)
    recipient = models.ForeignKey(User, related_name='message_recipients', blank=True, null=True)
    bid = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.text


class SwipeAction(DateHelper):
    user = models.ForeignKey(User)
    stuff = models.ForeignKey(Stuff)
    action = models.IntegerField(choices=action_choices)

    def __unicode__(self):
        return self.action


