from entity.UserAccount import UserAccount

class LoginController:
       
    
    def verifyAccount(self, email, password):
        
        userAccount = UserAccount()
        user, user_role, user_id = userAccount.verifyAccount(email,password)
        
        if user:
            return True, user_role, user_id
        else:
            return False, user_role, user_id
    
