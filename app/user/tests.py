from django.test import TestCase

from django.contrib.auth import get_user_model


def sample_user():
    return get_user_model().objects.create_user(
        'test@user.com',
    )


class UserModelTests(TestCase):
    """ Tests for User Model """

    def test_create_user(self):
        """ Test Creating a new user with email is successful """
        email = 'test@user.com'
        user = get_user_model().objects.create_user(email=email)
        self.assertEqual(user.email, email)

    def test_create_user_with_invalid_email(self):
        """ Test Creating user with invalid email address fails"""
        email = ''

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=email)

    def test_user_email_normalized(self):
        """ Test email normalized after creating a new user """
        email = 'test@USer.com'
        user = get_user_model().objects.create_user(email)

        self.assertEqual(user.email, email.lower())
