from django.test import TestCase

# Create your tests here.

from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighborhood , Profile , Business

class TestUser(TestCase):
    def setUp(self):
        self.testuser = User(username="user", email="test@mail.com")

    def test_instance(self):
        self.assertIsInstance(self.testuser, User)

    def test_save_user(self):
        self.assertFalse(self.testuser in User.objects.all())
        self.testuser.save()
        self.assertTrue(self.testuser in User.objects.all())

    def test_save_profile(self):
        self.fuser = User(username="fuser", email="carineuser@mail.com")
        self.fuser.save()
class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        """
        Function to test that profile is being saved
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)



class ProjecTestClass(TestCase):
    """  
    Tests Project class and its functions
    """
    def setUp(self):
        self.project = Project()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        """
        Function to test that a project is being saved
        """
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)




      

   