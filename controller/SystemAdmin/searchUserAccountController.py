from entity.UserAccount import UserAccount

class SearchUserAccountController:
    
    def searchUserAccount(self,email):
        
        userAccount = UserAccount()
        user = userAccount.searchUserAccount(email)
        
        return user;
        
    