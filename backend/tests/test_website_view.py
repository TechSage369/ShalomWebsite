import pytest
from django.test import Client
from django.urls import reverse


class TestViews:
    def test_homepage_status_code(self, request):
        client = Client()
        response = client.get(reverse('website:homepage'))
        assert respose.status_code == 200
    
    def test_about_us_status_code(self, request):
        client = Client()
        response = client.get(reverse('website:about_us'))
        assert response.status_code == 200
