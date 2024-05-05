from entity.UserProfile import UserProfile


class UserProfileController:
    
    def displayUserProfile(self,email):
        userProfileEntity = UserProfile()
        userObj = userProfileEntity.displayUserProfile(email)
        
        return userObj
    