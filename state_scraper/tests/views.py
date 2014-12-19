from django.contrib.auth.models import User
from django.test import TestCase, Client


class Scraper(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username="test", password="test")

    def test_login(self):
        response = self.client.login(username=u'test', password=u'test')
        assert False

    def test_unauthorized_login(self):
        response = self.client.login(username=u'unauthorized', password=u'unauthorized')
        assert False

    def test_logout(self):
        self.client.login(username=u'unauthorized', password=u'unauthorized')
        response = self.client.logout()
        assert False

    def test_home_endpoint(self):
        self.client.login(username=u'test', password=u'test')
        response = self.client.get('/home/')
        assert False

    def test_unauthorized_home_endpoint(self):
        self.client.login(username=u'unauthorized', password=u'unauthorized')
        response = self.client.get('/home/')
        assert False

    def test_geodata_endpoint(self):
        self.client.login(username=u'test', password=u'test')
        response = self.client.get('/geodata/')
        assert False

    def test_unauthorized_geodata_endpoint(self):
        self.client.login(username=u'unauthorized', password=u'unauthorized')
        response = self.client.get('/geodata/')
        assert False
