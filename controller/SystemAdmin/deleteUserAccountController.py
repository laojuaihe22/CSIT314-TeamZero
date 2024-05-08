from entity.UserAccount import UserAccount

class SuspendUserAccount:
    
    def suspendUserAccount(self, email):
    
        userAccount = UserAccount()
        is_suspend = userAccount.suspendUserAccount(email)
        
        if is_suspend:
            return True
        else:
            return False