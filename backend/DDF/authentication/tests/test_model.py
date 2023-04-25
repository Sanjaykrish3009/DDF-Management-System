from django.test import TestCase
from authentication.models import CustomUser
from django.db.utils import IntegrityError

class CustomUserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')

    def test_create_user(self):
        user = CustomUser.objects.get(email='test@gmail.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email=None, password='testpassword')

    def test_create_user_without_password(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='test@gmail.com', password=None)
    
    def test_duplicate_user(self):
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
    
    def test_get_user(self):
        user = CustomUser.objects.get(email='test@gmail.com')
        self.assertEqual(user, self.user)



