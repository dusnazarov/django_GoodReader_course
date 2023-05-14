from django.test import TestCase
from django.contrib.auth.models import User


class RegisterationTestcase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            "/users/register",
            
            data = {
                "username":'elyorjon',
                'first_name':"elyor1",
                'last_name':'dusnazarov1',
                'email':'elyor1.dusnazarov@gmail.com',
                'password':'1ed1115ed1'
            }
        )
        
        user = User.objects.get(username ="elyorjon")
        self.assertEqual(user.first_name, "elyor1")
        self.assertEqual(user.last_name, "dusnazarov1")
        self.assertEqual(user.email,"elyor1.dusnazarov@gmail.com")
        self.assertNotEqual(user.password,"1ed1115ed1")
        # self.assertTrue(user.check_password,"ed1115ed")
    
