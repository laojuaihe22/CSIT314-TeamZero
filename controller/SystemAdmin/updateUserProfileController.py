from entity.UserProfile import UserProfile

class UpdateUserProfileController:

    def updateUserProfile(self, email, field, data):

        if not email:
            return False 
    
        userProfile = UserProfile()
        updatedUser = userProfile.updateUserProfile(email, field, data)

        return updatedUser
        
