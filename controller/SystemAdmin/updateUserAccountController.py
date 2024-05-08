from entity.UserAccount import UserAccount

class UpdateUserAccountController:
    
    def updateUserAccount(self,user_email,field, value):
        
        userAccount = UserAccount()
        is_updated = userAccount.updateUserAccount(user_email,field, value)
        
        return is_updated