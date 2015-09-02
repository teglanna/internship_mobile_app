import json
from ..models import Image
from django.core.files import File
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory
from ..views import MessageViewSet, StuffViewSet, ImageViewSet, ActionViewSet
from .test_models import DataMixin


class MessagesViewTest(DataMixin, TestCase):

    def test_messages_empty_get(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('message-list'), content_type='application/json')

        view = MessageViewSet.as_view({'get': 'list'})
        resp = view(request)

        assert resp.status_code == 200
        assert resp.data['count'] == 0
        assert not resp.data['results']

    def test_messages_post(self):
        self.user.save()
        self.stuff.save()
        factory = APIRequestFactory()
        data = {
            'stuff': self.stuff.id,
            'author': self.user.id,
            'text': "test",
            'bid': 999
        }
        request = factory.post(reverse('message-list'), json.dumps(data), content_type='application/json')

        view = MessageViewSet.as_view({'post': 'create'})
        resp = view(request)

        assert resp.status_code == 201
        assert resp.data['text'] == data['text']
        assert resp.data['bid'] == data['bid']
        assert resp.data['author'] == self.user.id
        assert resp.data['stuff'] == self.stuff.id

    def test_messages_get_results(self):
        self.user.save()
        self.stuff.save()
        factory = APIRequestFactory()
        data = {
            'stuff': self.stuff.id,
            'author': self.user.id,
            'text': "test",
            'bid': 999
        }
        request_post = factory.post(reverse('message-list'), json.dumps(data), content_type='application/json')
        view = MessageViewSet.as_view({'post': 'create'})
        resp = view(request_post)

        assert resp.status_code == 201

        request_get = factory.get(reverse('message-list'), content_type='application/json')

        view = MessageViewSet.as_view({'get': 'list'})
        resp = view(request_get)

        results = resp.data['results'][0]

        assert resp.status_code == 200
        assert resp.data['count'] == 1
        assert results['stuff'] == self.stuff.id
        assert results['author'] == self.user.id
        assert results['bid'] == data['bid']
        assert results['text'] == data['text']

    def test_messages_get_detail(self):
        self.user.save()
        self.stuff.save()
        factory = APIRequestFactory()
        data = {
            'stuff': self.stuff.id,
            'author': self.user.id,
            'text': "test",
            'bid': 999
        }
        request_post = factory.post(reverse('message-list'), json.dumps(data), content_type='application/json')
        view = MessageViewSet.as_view({'post': 'create'})
        resp = view(request_post)

        assert resp.status_code == 201

        item_created_id = resp.data['id']
        factory = APIRequestFactory()
        request = factory.get(reverse('message-detail', kwargs={'pk': item_created_id}), content_type='application/json')

        view = MessageViewSet.as_view({'get': 'retrieve'})
        resp = view(request, pk=item_created_id)

        assert resp.status_code == 200
        assert resp.data['id'] == item_created_id
        assert resp.data['stuff'] == self.stuff.id
        assert resp.data['author'] == self.user.id
        assert resp.data['text'] == data['text']
        assert resp.data['bid'] == data['bid']



class StuffViewTest(DataMixin, TestCase):

    def test_stuffs_empty_get(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('stuff-list'), content_type='application/json')

        view = StuffViewSet.as_view({'get': 'list'})
        resp = view(request)

        assert resp.status_code == 200
        assert resp.data['count'] == 0
        assert not resp.data['results']

    def test_stuffs_post(self):
        self.user.save()
        factory = APIRequestFactory()
        data = {
            'user': self.user.id,
            'location': str(self.ref_location),
            'description': "test",
            'pickup': True,
            'delivery': False,
            'price': 999,
            'active': True
        }
        request = factory.post(reverse('stuff-list'), json.dumps(data), content_type='application/json')

        view = StuffViewSet.as_view({'post': 'create'})
        resp = view(request)

        assert resp.status_code == 201
        assert resp.data['user'] == self.user.id
        assert resp.data['location'] == data['location']
        assert resp.data['description'] == data['description']
        assert resp.data['pickup'] == data['pickup']
        assert resp.data['delivery'] == data['delivery']
        assert resp.data['price'] == data['price']
        assert resp.data['active'] == data['active']

    def test_stuffs_get_results(self):
        self.user.save()
        factory = APIRequestFactory()
        data = {
            'user': self.user.id,
            'location': str(self.ref_location),
            'description': "test",
            'pickup': True,
            'delivery': False,
            'price': 999,
            'active': True
        }

        request_post = factory.post(reverse('stuff-list'), json.dumps(data), content_type='application/json')
        view = StuffViewSet.as_view({'post': 'create'})
        resp = view(request_post)

        assert resp.status_code == 201

        request_get = factory.get(reverse('stuff-list'), content_type='application/json')

        view = StuffViewSet.as_view({'get': 'list'})
        resp = view(request_get)

        results = resp.data['results'][0]

        assert resp.status_code == 200
        assert resp.data['count'] == 1
        assert results['user'] == self.user.id
        assert results['location'] == data['location']
        assert results['description'] == data['description']
        assert results['pickup'] == data['pickup']
        assert results['delivery'] == data['delivery']
        assert results['price'] == data['price']
        assert results['active'] == data['active']

    def test_stuffs_get_detail(self):
        self.user.save()
        factory = APIRequestFactory()
        data = {
            'user': self.user.id,
            'location': str(self.ref_location),
            'description': "test",
            'pickup': True,
            'delivery': False,
            'price': 999,
            'active': True
        }
        request_post = factory.post(reverse('stuff-list'), json.dumps(data), content_type='application/json')
        view = StuffViewSet.as_view({'post': 'create'})
        resp = view(request_post)

        assert resp.status_code == 201

        item_created_id = resp.data['id']
        factory = APIRequestFactory()
        request = factory.get(reverse('stuff-detail', kwargs={'pk': item_created_id}), content_type='application/json')

        view = StuffViewSet.as_view({'get': 'retrieve'})
        resp = view(request, pk=item_created_id)

        assert resp.status_code == 200
        assert resp.data['user'] == self.user.id
        assert resp.data['location'] == data['location']
        assert resp.data['description'] == data['description']
        assert resp.data['pickup'] == data['pickup']
        assert resp.data['delivery'] == data['delivery']
        assert resp.data['price'] == data['price']
        assert resp.data['active'] == data['active']



class ActionViewTest(DataMixin, TestCase):

    def test_actions_post(self):
        self.user.save()
        self.stuff.save()
        factory = APIRequestFactory()
        data = {
            'user': self.user.id,
            'stuff': self.stuff.id,
            'action': 0
        }
        request = factory.post(reverse('swipeaction-list'), json.dumps(data), content_type='application/json')

        view = ActionViewSet.as_view({'post': 'create'})
        resp = view(request)

        assert resp.status_code == 201
        assert resp.data['user'] == self.user.id
        assert resp.data['stuff'] == self.stuff.id
        assert resp.data['action'] == data['action']


    def test_actions_get_results(self):
        self.user.save()
        self.stuff.save()
        factory = APIRequestFactory()
        data = {
            'user': self.user.id,
            'stuff': self.stuff.id,
            'action': 0
        }

        request_post = factory.post(reverse('swipeaction-list'), json.dumps(data), content_type='application/json')
        view = ActionViewSet.as_view({'post': 'create'})
        resp = view(request_post)

        assert resp.status_code == 201

        request_get = factory.get(reverse('swipeaction-list'), content_type='application/json')
        view = ActionViewSet.as_view({'get': 'list'})
        resp = view(request_get)

        results = resp.data['results'][0]

        assert resp.status_code == 200
        assert resp.data['count'] == 1
        assert results['user'] == self.user.id
        assert results['stuff'] == self.stuff.id
        assert results['action'] == data['action']


    def test_actions_get_detail(self):
        self.user.save()
        self.stuff.save()
        factory = APIRequestFactory()
        data = {
            'user': self.user.id,
            'stuff': self.stuff.id,
            'action': 0
        }

        request_post = factory.post(reverse('swipeaction-list'), json.dumps(data), content_type='application/json')
        view = ActionViewSet.as_view({'post': 'create'})
        resp = view(request_post)

        assert resp.status_code == 201

        item_created_id = resp.data['id']
        factory = APIRequestFactory()
        request = factory.get(reverse('swipeaction-detail', kwargs={'pk': item_created_id}), content_type='application/json')

        view = ActionViewSet.as_view({'get': 'retrieve'})
        resp = view(request, pk=item_created_id)


        assert resp.status_code == 200
        assert resp.data['id'] == item_created_id
        assert resp.data['user'] == self.user.id
        assert resp.data['stuff'] == self.stuff.id
        assert resp.data['action'] == data['action']


class ImageViewTest(DataMixin, TestCase):

    def test_images_empty_get(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('image-list'), content_type='application/json')

        view = ImageViewSet.as_view({'get': 'list'})
        resp = view(request)

        assert resp.status_code == 200
        assert resp.data['count'] == 0
        assert not resp.data['results']


    def test_images_post(self):
        dummy_image_file = File(open(__file__, 'rb'), 'testimage2.jpg')
        image = Image.objects.create(image=dummy_image_file, stuff=self.stuff)

        factory = APIRequestFactory()
        data = {
            'stuff': self.stuff.id,
            'image': dummy_image_file.name
        }

        request = factory.post(reverse('image-list'), json.dumps(data), content_type='application/json')

        view = ImageViewSet.as_view({'post': 'create'})
        resp = view(request)

#       import pdb; pdb.set_trace() 

        assert resp.status_code == 201
        assert resp.data['stuff'] == self.stuff.id
        assert resp.data['image'] == data['image']

        os.remove('testimage2.jpg')


#     def test_images_get_results(self):
#         self.stuff.save()
#         factory = APIRequestFactory()
#         data = {
#             'stuff': self.stuff.id,
#             'image': '1.jpg'
#         }
   
#         request_post = factory.post(reverse('image-list'), json.dumps(data), content_type='application/json')
#         view = ImageViewSet.as_view({'post': 'create'})
#         resp = view(request_post)

#         assert resp.status_code == 201

#         request_get = factory.get(reverse('image-list'), content_type='application/json')

#         view = ImageViewSet.as_view({'get': 'list'})
#         resp = view(request_get)

#         results = resp.data['results'][0]

#         assert resp.status_code == 200
#         assert resp.data['count'] == 1
#         assert results['stuff'] == self.stuff.id
#         assert results['image'] == data['image']


#     def test_images_get_detail(self):
#         self.stuff.save()
#         factory = APIRequestFactory()
#         data = {
#             'stuff': self.stuff.id,
#             'image': '1.jpg'
#         }
#         request_post = factory.post(reverse('image-list'), json.dumps(data), content_type='application/json')
#         view = ImageViewSet.as_view({'post': 'create'})
#         resp = view(request_post)

#         assert resp.status_code == 400

#         item_created_id = resp.data['id']
#         factory = APIRequestFactory()
#         request = factory.get(reverse('image-detail', kwargs={'pk': item_created_id}), content_type='application/json')

#         view = ImageViewSet.as_view({'get': 'retrieve'})
#         resp = view(request, pk=item_created_id)

#         assert resp.status_code == 200
#         assert resp.data['id'] == item_created_id
#         assert resp.data['stuff'] == self.stuff.id
#         assert resp.data['image'] == data['image']
#         # ?self.image.name
        


