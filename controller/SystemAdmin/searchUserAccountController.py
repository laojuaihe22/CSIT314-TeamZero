from entity.UserAccount import User

class SearchUserAccountController:
    
    def getUserAccount(self,email):
        
        userAccount = User()
        user = userAccount.getUserAccount(email)
        
        return user;
        
    