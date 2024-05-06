from entity.UserProfile import UserProfile


class UserProfileController:
    
    def viewUserProfile(self,email):
        userProfileEntity = UserProfile()
        userObj = userProfileEntity.viewUserProfile(email)
        
        return userObj
    