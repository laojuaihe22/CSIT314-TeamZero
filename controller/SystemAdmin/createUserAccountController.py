from entity.UserAccount import UserAccount
class CreateUserAccountController:
    
    def createUserAccount(self,user_email,user_pass,role):
        
        userAccount = UserAccount()
        isCreated = userAccount.createUserAccount(user_email,user_pass,role)
        
        return isCreated
        
    