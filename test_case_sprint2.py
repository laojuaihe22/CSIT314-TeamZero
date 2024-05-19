from entity.UserAccount import UserAccount
import unittest
from entity.UserProfile import UserProfile


class TestUserAccountFunctions(unittest.TestCase):
    def setUp(self):
        # Initialize your class instance
        self.user_account = UserAccount()
        self.user_profile = UserProfile()

    def test_createUserAccount(self):
        # Test creating a new user account
        email = "test@example.com"
        password = "password123"
        role = "admin"  
        result = self.user_account.createUserAccount(email, password, role)
        self.assertTrue(result)  # Check if user account creation is successful

        # Test creating a user account with an existing email
        result = self.user_account.createUserAccount(email, password, role)
        self.assertFalse(result)  # Check if user account creation fails for existing email

    def test_suspendUserAccount(self):
        # Test suspending an existing user account
        email = "test@example.com"
        self.user_account.createUserAccount(email, "password123", "user")
        result = self.user_account.suspendUserAccount(email)
        self.assertTrue(result)  # Check if user account suspension is successful

        # Test suspending a non-existing user account
        result = self.user_account.suspendUserAccount("nonexistent@example.com")
        self.assertFalse(result)  # Check if user account suspension fails for non-existing email

    def test_updateUserAccount(self):
        # Test updating an existing user account
        email = "test@example.com"
        self.user_account.createUserAccount(email, "password123", "user")
        result = self.user_account.updateUserAccount(email, "password", "newpassword123")
        self.assertTrue(result)  # Check if user account update is successful

        # Test updating a non-existing user account
        result = self.user_account.updateUserAccount("nonexistent@example.com", "password", "newpassword123")
        self.assertFalse(result)  # Check if user account update fails for non-existing email

    def test_viewUserAccountData(self):
        # Test viewing user account data
        result = self.user_account.viewUserAccountData()
        self.assertIsInstance(result, list)  # Check if the result is a list

    def test_searchUserAccount(self):
        # Test searching for an existing user account
        email = "test@example.com"
        self.user_account.createUserAccount(email, "password123", "user")
        result = self.user_account.searchUserAccount(email)
        self.assertTrue(result)  # Check if search returns user data

        # Test searching for a non-existing user account
        result = self.user_account.searchUserAccount("nonexistent@example.com")
        self.assertFalse(result)  # Check if search returns False for non-existing email
        
    def test_createUserProfile(self):
        # Test creating a new user profile
        email = "test@example.com"
        name = "Test User"
        description = "Test description"
        result = self.user_profile.createUserProfile(email, name, description)
        self.assertTrue(result)  # Check if user profile creation is successful

        # Test creating a user profile for a non-existing user
        result = self.user_profile.createUserProfile("nonexistent@example.com", name, description)
        self.assertFalse(result)  # Check if user profile creation fails for non-existing email

    def test_adminViewUserProfile(self):
        # Test viewing user profile data
        result = self.user_profile.adminViewUserProfile()
        self.assertIsInstance(result, list)  # Check if the result is a list

    def test_suspendUserProfile(self):
        # Test suspending an existing user profile
        email = "test@example.com"
        result = self.user_profile.suspendUserProfile(email)
        self.assertTrue(result)  # Check if user profile suspension is successful

        # Test suspending a non-existing user profile
        result = self.user_profile.suspendUserProfile("nonexistent@example.com")
        self.assertFalse(result)  # Check if user profile suspension fails for non-existing email

    def test_searchUserProfile(self):
        # Test searching for an existing user profile
        email = "test@example.com"
        self.user_profile.createUserProfile(email, "Test User", "Test description")
        result = self.user_profile.searchUserProfile(email)
        self.assertTrue(result)  # Check if search returns user profile data

        # Test searching for a non-existing user profile
        result = self.user_profile.searchUserProfile("nonexistent@example.com")
        self.assertFalse(result)  # Check if search returns False for non-existing email

    def test_updateUserProfile(self):
        # Test updating an existing user profile
        email = "test@example.com"
        self.user_profile.createUserProfile(email, "Test User", "Test description")
        result = self.user_profile.updateUserProfile(email, "description", "Updated description")
        self.assertTrue(result)  # Check if user profile update is successful

        # Test updating a non-existing user profile
        result = self.user_profile.updateUserProfile("nonexistent@example.com", "description", "Updated description")
        self.assertFalse(result)  # Check if user profile update fails for non-existing email

if __name__ == '__main__':
    unittest.main()
