from entity.UserAccount import User

class SignUpController:
    
    def signUpUser(self,email,password):
        
        userAccount = User()
        is_created = userAccount.signUpUser(email,password)
        
        return is_created