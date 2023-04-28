from django.db import IntegrityError
from django.test import TestCase
from user.models import UserProfile
from authentication.models import CustomUser

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@gmail.com', password='testpassword')
        self.userprofile = UserProfile(user=self.user,first_name='firstname',last_name='lastname',user_type='faculty')

    def test_create_userprofile(self):
        self.assertEqual(self.userprofile.user,self.user)
        self.assertEqual(self.userprofile.first_name,'firstname')
        self.assertEqual(self.userprofile.last_name,'lastname')
        self.assertEqual(self.userprofile.user_type,'faculty')

    def test_create_userprofile_without_user(self):
        with self.assertRaises(IntegrityError):
            userprofile = UserProfile(first_name='firstname',last_name='lastname',user_type='faculty')
            userprofile.save()

    def test_get_user_profile(self):
        userprofile = self.userprofile.get_user_profile()
        self.assertEqual(userprofile['firstname'],'firstname')
        self.assertEqual(userprofile['lastname'],'lastname')
        self.assertEqual(userprofile['email'],'test@gmail.com')

    def test_get_user_type(self):
        user_type = self.userprofile.get_user_type()
        self.assertEqual(user_type,'faculty')
