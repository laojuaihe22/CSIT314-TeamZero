from entity.UserAccount import UserAccount

class SuspendUserAccountController:
    
    def suspendUserAccount(self, user_email):
    
        userAccount = UserAccount()
        is_suspend = userAccount.suspendUserAccount(user_email)
        
        if is_suspend:
            return True
        else:
            return False