from entity.UserProfile import UserProfile

class UpdateUserProfileController:

    def updateUserProfile(self, user_email, field, value):

        userProfile = UserProfile()
        updatedUser = userProfile.updateUserProfile(user_email, field, value)

        return updatedUser
        
