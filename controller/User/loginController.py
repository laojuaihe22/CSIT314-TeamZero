from entity.UserAccount import UserAccount

class LoginController:
       
    
    def verifyAccount(self, email, password):
        
        userAccount = UserAccount()
        user, user_role = userAccount.verifyAccount(email,password)
        
        if user:
            return True, user_role
        else:
            return False, user_role;
    
