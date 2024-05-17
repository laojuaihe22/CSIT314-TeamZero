from entity.UserAccount import UserAccount
import unittest

class Test_case_sprint1(unittest.TestCase):
    
    def test_success_login(self):
        verification = UserAccount().verifyAccount("admin@gmail.com", "1")
        self.assertEqual(verification[0],True)

    def test_fail_login(self):
        verification = UserAccount().verifyAccount("fake@gmail.com", "1")
        self.assertEqual(verification[0],False)
        
if __name__ == '__main__':
    unittest.main()

