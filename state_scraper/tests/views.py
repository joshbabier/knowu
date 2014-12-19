import json
from django.contrib.auth.models import User
from django.test import TestCase, Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username="test", password="test")

    def test_root_endpoint_returns_login(self):
        """
        A user should get to the login if they hit the root url
        :return:
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_home_endpoint(self):
        """
        Make sure a logged in user can access the home page.
        :return:
        """
        self.client.login(username=u'test', password=u'test')
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scraper/home.html')

    def test_unauthorized_home_endpoint(self):
        """
        Make sure an unauthorized user cannot get to the home page
        :return:
        """
        self.client.login(username=u'unauthorized', password=u'unauthorized')
        response = self.client.get('/home/')
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'scraper/home.html')

    def test_geodata_endpoint_with_state_parameter(self):
        """
        Should be able to see geolocation data for a given state
        :return:
        """
        self.client.login(username=u'test', password=u'test')
        response = self.client.get('/geodata/?state=AZ')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scraper/geodata.html')

    def test_geodata_endpoint_without_state_parameter(self):
        """
        Should not be able to see geolocation data if a state is not given.
        :return:
        """
        self.client.login(username=u'test', password=u'test')
        response = self.client.get('/geodata/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scraper/home.html')

    def test_unauthorized_geodata_endpoint(self):
        """
        Should not be able to see geolocation data if a user is not authorized
        :return:
        """
        self.client.login(username=u'unauthorized', password=u'unauthorized')
        response = self.client.get('/geodata/')
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'scraper/home.html')
        self.assertTemplateNotUsed(response, 'scraper/geodata.html')
