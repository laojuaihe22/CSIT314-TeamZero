from entity.UserAccount import UserAccount
class CreateUserAccountController:
    
    def createUserAccount(self,user_email,user_pass,user_role):
        
        userAccount = UserAccount()
        isCreated = userAccount.createUserAccount(user_email,user_pass,user_role)
        
        if isCreated:
            return True
        else:
            return False
        
    