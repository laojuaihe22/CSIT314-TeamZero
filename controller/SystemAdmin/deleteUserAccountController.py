from entity.UserAccount import UserAccount

class DeleteUserAccount:
    
    def deleteUserAccount(self, email):
        
        if not email:
            return False 
        
        userAccount = UserAccount()
        isDeleted = userAccount.deleteUserAccount(email)
        
        if isDeleted:
            return True
        else:
            return False