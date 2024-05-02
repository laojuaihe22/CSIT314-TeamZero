from entity.UserAccount import User

class LoginController:
       
    
    def verifyAccount(self, email, password):
        
        userAccount = User()
        user, user_role = userAccount.verifyAccount(email,password)
        
        if user:
            return True, user_role
        else:
            return False, user_role;
    
