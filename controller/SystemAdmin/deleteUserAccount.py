from entity.UserAccount import User

class DeleteUserAccount:
    
    def deleteUserAccount(self, email):
        
        if not email:
            return False 
        
        userAccount = User()
        isDeleted = userAccount.deleteUserAccount(email)
        
        if isDeleted:
            return True
        else:
            return False