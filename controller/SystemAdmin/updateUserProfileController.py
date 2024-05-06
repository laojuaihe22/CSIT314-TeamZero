from entity.UserProfile import UserProfile

class UpdateUserProfileController:

    def updateUserProfile(self, email, field, data):

        if not email:
            return False 
        

        userProfile = UserProfile()
        isUpdated = userProfile.updateUserProfile(email, field, data)

        if isUpdated:
            return True
        else:
            return False
        
