from entity.UserAccount import UserAccount

class ViewUserAccountController:
    
    def viewUserAccountData(self):
        userAccount = UserAccount()
        user_account = userAccount.viewUserAccountData()
        
        return user_account