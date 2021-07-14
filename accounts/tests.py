from django.test import TestCase
from django.contrib.auth import get_user_model


class django_custom_user_test(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='ayman',
            email='ayman_naif@hotmail.com',
            password='ayman123456'
        )

    def test_create_new_user(self):

        self.assertEquals(self.user.email, 'ayman_naif@hotmail.com')
        self.assertEquals(self.user.username, 'ayman')

    def test_duplicate_emails(self):
        try:

            self.user2 = get_user_model().objects.create_user(
                username='ayman',
                email='ayman_naif@hotmail.com',
                password='ayman123456'
            )

        except:
            print('This email is registered')
