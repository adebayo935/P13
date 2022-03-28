from django.test import TestCase
from django.urls import reverse


class IndexTestCase(TestCase):
    def test_should_showIndex(self):
        response = reverse('index')
        assert response == "/"
