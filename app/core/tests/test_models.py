from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """This test tests whether creating new user is successful"""

        email = "test@codernaga.com"
        password = "password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test if the new user is normalized"""
        email = "test@CODERNAGA.COM"
        user = get_user_model().objects.create_user(
            email,
            "test123"
        )
        self.assertEqual(user.email, email.lower())

    def test_valid_user_email(self):
        """Tests if users have a valid email. Raises error if no or None email is provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_superuser(self):
        """Test creating a new super user"""

        user = get_user_model().objects.create_super_user(
            "test@nagasai.com",
            "test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
