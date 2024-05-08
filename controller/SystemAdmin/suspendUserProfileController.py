from entity.UserProfile import UserProfile


class SuspendUserProfile:

    def suspendUserProfile(self, email):
          
        if not email:
                return False 
        
        userProfile = UserProfile()
        isDeleted = userProfile.suspendUserProfile(email)
        
        return isDeleted
              