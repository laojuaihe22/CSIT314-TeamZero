from entity.UserAccount import UserAccount
import unittest

from app import app

class Test_case_sprint1(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_admin_success_login(self):
        verification = UserAccount().verifyAccount("admin@gmail.com", "1")
        self.assertEqual(verification[0],True)
        self.assertEqual(verification[1],"admin")
        
    def test_real_estate_agent_success_login(self):
        verification = UserAccount().verifyAccount("rea@gmail.com", "1")
        self.assertEqual(verification[0],True)
        self.assertEqual(verification[1],"rea")
        
    def test_buyer_success_login(self):
        verification = UserAccount().verifyAccount("buyer@gmail.com", "1")
        self.assertEqual(verification[0],True)
        self.assertEqual(verification[1],"buyer")
        
    def test_seller_success_login(self):
        verification = UserAccount().verifyAccount("seller@gmail.com", "1")
        self.assertEqual(verification[0],True)
        self.assertEqual(verification[1],"seller")
        
    def test_admin_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302) # Check if the response is a redirect
        self.assertIn('/', response.headers['Location']) # Check if the redirect location is '/'

        
    def test_real_estate_agent_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302) # Check if the response is a redirect
        self.assertIn('/', response.headers['Location']) # Check if the redirect location is '/'
        
    def test_buyer_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302) # Check if the response is a redirect
        self.assertIn('/', response.headers['Location']) # Check if the redirect location is '/'
        
    def test_seller_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302) # Check if the response is a redirect
        self.assertIn('/', response.headers['Location']) # Check if the redirect location is '/'
    
if __name__ == '__main__':
    unittest.main()

