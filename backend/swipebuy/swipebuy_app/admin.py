from django.contrib import admin
from .models import Stuff, Message, SwipeAction, Image, CheckIn


admin.site.register(Stuff)
admin.site.register(Message)
admin.site.register(SwipeAction)
admin.site.register(Image)
admin.site.register(CheckIn)