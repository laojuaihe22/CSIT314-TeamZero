from entity.UserProfile import UserProfile

class CreateUserProfileController():

    def createUserProfile(self, user_email, user_name, user_description):
        
        userProfile = UserProfile()
        isCreated = userProfile.createUserProfile(user_email, user_name, user_description)
        
        return isCreated
            