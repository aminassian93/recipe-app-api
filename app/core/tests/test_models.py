from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """"Test Creating A New User With An Email Is Successful"""
        email = "armen1222@yahoo.com"
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test The Email For A New Usr Is Normalized"""
        email = 'test@YAHOO.COM'
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test Creating User With No Email Raises Error"""
        ### Anything that we run in here should raise a value error
        with self.assertRaises(ValueError):
                get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        """Test Creating A New Superuser"""
        user = get_user_model().objects.create_superuser(
            email = "test@yahoo.com",
            password = 'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
