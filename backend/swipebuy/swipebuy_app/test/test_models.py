from datetime import datetime
import os
from django.contrib.auth.models import User
from django.core.files import File
from django.test import TestCase
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from swipebuy_app.models import Stuff, CheckIn, SwipeAction, Message, Image


class UserStuffMixin(object):
    user, created = User.objects.get_or_create(username="test", password="test", is_superuser=True, email="test@test.com")
    ref_location = Point(1.232433, 1.2323232)
    stuff = Stuff.objects.create(user=user, location=ref_location, description="test", price=999)
    assert user
    assert stuff


class TestCaseModels(UserStuffMixin, TestCase):
    def test_stuff_object(self):
        assert isinstance(self.stuff.modified, datetime)
        assert isinstance(self.stuff.created, datetime)
        assert self.stuff.price == 999
        assert self.stuff.description == 'test'
        assert self.stuff.user == self.user
        assert self.stuff.location == self.ref_location
        assert self.stuff.main_img is None

    def test_create_checkin(self):
        ref_location = Point(1.232433, 1.2323232)
        checkin = CheckIn.objects.create(user=self.user,location=ref_location)

        assert checkin
        assert isinstance(checkin.modified, datetime)
        assert isinstance(checkin.created, datetime)
        assert checkin.user == self.user
        assert checkin.location == ref_location

    def test_swipe_action(self):
        action_choice = SwipeAction.SWIPING
        swipe = SwipeAction.objects.create(user=self.user, stuff=self.stuff, action=action_choice)

        assert swipe
        assert swipe.stuff == self.stuff
        assert swipe.stuff.location == self.ref_location
        assert swipe.user == self.user
        assert swipe.action == action_choice

    def test_create_message(self):
        bid = 1009
        msg = "well hello"
        message = Message.objects.create(author=self.user, stuff=self.stuff, text=msg, bid=bid)

        assert message
        assert message.author == self.user
        assert message.stuff == self.stuff
        assert message.text == msg
        assert message.bid == bid
        assert message.recipient is None

        bid = 1019
        msg = "yo hello"
        user2, created = User.objects.get_or_create(username="test2", password="test2", is_superuser=True, email="test2@test.com")
        message2 = Message.objects.create(author=user2, stuff=self.stuff, text=msg, bid=bid, recipient=self.user)

        assert message2
        assert message2.author == user2
        assert message2.stuff == self.stuff
        assert message2.text == msg
        assert message2.bid == bid
        assert message2.recipient == self.user

        print message
        print message2

    def test_create_image(self):
        dummy_image_file = File(open(__file__, 'rb'), 'testimage.jpg')

        image = Image.objects.create(image=dummy_image_file, stuff=self.stuff)

        assert image
        self.assertIn("testimage.jpg", image.image.name)
        assert image.stuff == self.stuff

        # remove temp file
        os.remove(dummy_image_file.name)

    def create_stuff_with_main_image(self):
        dummy_image_file = File(open(__file__, 'rb'), 'testimage.jpg')

        image = Image.objects.create(image=dummy_image_file, stuff=self.stuff)

        stuff = Stuff.objects.create(user=self.user, location=self.ref_location, description="tes21t", price=1000, main_img=image)

        assert stuff
        assert stuff.main_img == image
