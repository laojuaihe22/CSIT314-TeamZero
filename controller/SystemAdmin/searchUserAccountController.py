from entity.UserAccount import User

class SearchUserAccountController:
    
    def searchUserAccount(self,email):
        
        userAccount = User()
        user = userAccount.searchUserAccount(email)
        
        return user;
        
    