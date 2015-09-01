import json
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory
from ..views import MessageViewSet, StuffViewSet
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
            'main_img': 'picture.jpg',
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
        assert resp.data['main_img'] == data['main_img']
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
            'main_img': 'picture.jpg',
            'active': True
        }

        request_post = factory.post(reverse('stuff-list'), json.dumps(data), content_type='application/json')
        view = StuffViewSet.as_view({'post': 'create'})
        resp = view(request_post)

        assert resp.status_code == 201

        request_get = factory.get(reverse('stuff-list'), content_type='application/json')

        view = StuffViewSet.as_view({'get': 'list'})
        resp = view(request_get)

        # import pdb; pdb.set_trace()


        results = resp.data['results'][0]

        assert resp.status_code == 200
        assert resp.data['count'] == 1
        assert results['user'] == self.user.id
        assert results['location'] == data['location']
        assert results['description'] == data['description']
        assert results['pickup'] == data['pickup']
        assert results['delivery'] == data['delivery']
        assert results['price'] == data['price']
        assert results['main_img'] == data['main_img']
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
            'main_img': 'picture.jpg',
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
        assert resp.data['main_img'] == data['main_img']
        assert resp.data['active'] == data['active']
