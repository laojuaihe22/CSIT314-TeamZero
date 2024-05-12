from entity.UserProfile import UserProfile


class SuspendUserProfileController:

    def suspendUserProfile(self, user_email):
        
        
        userProfile = UserProfile()
        isDeleted = userProfile.suspendUserProfile(user_email)
        
        return isDeleted
              