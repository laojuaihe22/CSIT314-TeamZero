from entity.UserProfile import UserProfile

class ViewUserProfileController():

    def viewUserProfile(self):
        userProfiles = UserProfile()
        user_profiles = userProfiles.adminViewUserProfile()
        
        return user_profiles