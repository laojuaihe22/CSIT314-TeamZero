from entity.PropertyListing import PropertyListing

class ViewPropertyListingController():

    def viewPropertyListingbyId(self, user_id):
        
        propertyListing = PropertyListing()
        property_list = propertyListing.viewPropertyListingbyId(user_id)

        return property_list