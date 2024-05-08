from entity.UserProfile import UserProfile

class CreateUserProfileController():

    def createUserProfile(self, email, name, description):

        if not email or not name or not description:
            return False 
        
        userProfile = UserProfile()
        isCreated = userProfile.createUserProfile(email, name, description)
        
        return isCreated
            