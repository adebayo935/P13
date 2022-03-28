from django.test import TestCase
from django.urls import reverse


class ProfileTestCase(TestCase):
    def test_should_showIndex(self):
        response = reverse('profiles_index')
        assert response == "/profiles/"

    def test_should_showProfile(self):
        response = reverse('profile', args=['4meRomance'])
        assert response == "/profiles/4meRomance/"
