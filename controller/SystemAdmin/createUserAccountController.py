from entity.UserAccount import UserAccount
class CreateUserController:
    
    def createUserAccount(self,email,password,role):
        
        if not email or not password or not role:
            return False 
        
        userAccount = UserAccount()
        isCreated = userAccount.createUserAccount(email,password,role)
        
        if isCreated:
            return True
        else:
            return False
        
    