from django.test import TestCase
from django.urls import reverse


class LettingTestCase(TestCase):
    def test_should_showIndex(self):
        response = reverse('lettings_index')
        assert response

    def test_should_showLetting(self):
        response = reverse('letting', args=[1])
        assert response
