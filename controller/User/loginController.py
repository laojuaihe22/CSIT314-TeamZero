from entity.UserAccount import User

class LoginController:
       
    
    def verifyAccount(self, email, password):
        # Check if username or password is empty
        if not email or not password:
            return False  # If either username or password is empty, return False
        
        userAccount = User()
        user, user_role = userAccount.verifyAccount(email,password)
        
        if user:
            return True, user_role
        else:
            return False, user_role;
    
