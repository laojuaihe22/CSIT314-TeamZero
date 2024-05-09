from entity.UserAccount import UserAccount
class CreateUserAccountController:
    
    def createUserAccount(self,email,password,role):
        
        userAccount = UserAccount()
        isCreated = userAccount.createUserAccount(email,password,role)
        
        if isCreated:
            return True
        else:
            return False
        
    