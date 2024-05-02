from entity.UserAccount import User

class ViewUserAccountController:
    
    def getUserAccountData(self):
        userAccount = User()
        user_account = userAccount.getUserAccountData()
        
        return user_account