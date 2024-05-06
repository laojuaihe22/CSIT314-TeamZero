from entity.UserProfile import UserProfile

class CreateUserProfileController():

    def createUserProfile(self, email, name, age, description):

        if not email or not name or not age:
            return False 
        
        userProfile = UserProfile()
        isCreated = userProfile.createUserProfile(email, name, age, description)
        
        if isCreated:
            return True
        else:
            return False