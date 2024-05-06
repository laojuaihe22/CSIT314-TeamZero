from entity.UserProfile import UserProfile


class DeleteUserProfile:

    def deleteUserProfile(self, email):
          
        if not email:
                return False 
        
        userProfile = UserProfile()
        isDeleted = userProfile.deleteUserProfile(email)
        
        if isDeleted:
            return True
        else:
            return False