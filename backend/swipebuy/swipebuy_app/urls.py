from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)
router.register(r'stuffs', views.StuffViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'actions', views.ActionViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
