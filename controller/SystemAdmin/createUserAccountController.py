from entity.UserAccount import User
class CreateUserController:
    
    def createUserAccount(self,email,password,role):
        
        if not email or not password or not role:
            return False 
        
        userAccount = User()
        isCreated = userAccount.createUserAccount(email,password,role)
        
        if isCreated:
            return True
        else:
            return False
        
    