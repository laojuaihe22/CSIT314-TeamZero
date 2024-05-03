from entity.UserAccount import User

class ViewUserAccountController:
    
    def viewUserAccountData(self):
        userAccount = User()
        user_account = userAccount.viewUserAccountData()
        
        return user_account