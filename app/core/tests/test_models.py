from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_With_email_successful(self):
        """ Test creates new user with email"""
        email = 'test@abc.com'
        password = 'testpwd123'
        user= get_user_model().objects.create_user(
            email=email,
            password= password  
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalised"""
        email ="test@ABC.com"
        user =get_user_model().objects.create_user(email,"testpwd123") 

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"testpwd123") 

    def test_create_new_superuser(self):
        """ Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@abc.com",
            "testpwd123"
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
