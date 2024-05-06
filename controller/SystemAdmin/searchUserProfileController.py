from entity.UserProfile import UserProfile

class SearchUserProfileController:

    def searchUserProfile(self,email):

        userProfile = UserProfile()
        user = userProfile.searchUserProfile(email)

        return user