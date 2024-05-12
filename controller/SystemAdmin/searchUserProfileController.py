from entity.UserProfile import UserProfile

class SearchUserProfileController:

    def searchUserProfile(self,user_email):

        userProfile = UserProfile()
        user = userProfile.searchUserProfile(user_email)

        return user