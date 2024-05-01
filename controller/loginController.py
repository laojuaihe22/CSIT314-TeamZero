from entity.UserAccount import User
class LoginController:
    
    def __init__(self):
        self.role = None
        
    
    def verifyAccount(self, email, password):
        # Check if username or password is empty
        if not email or not password:
            return False  # If either username or password is empty, return False
        
        userAccount = User()
        user = userAccount.verifyAccount(email,password)
        
        if user:
            self.role = userAccount.getUserRole()
            return True
        else:
            False;
    
    def getUserRole(self):
        return self.role