from entity.UserAccount import UserAccount

class SignUpController:
    
    def signUpUser(self,email,password):
        
        userAccount = UserAccount()
        is_created = userAccount.signUpUser(email,password)
        
        return is_created