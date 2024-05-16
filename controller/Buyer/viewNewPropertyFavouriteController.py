from entity.PropertyListing import PropertyListing

class ViewNewPropertyFavouriteController:
    
    
    def buyerViewFavouriteNewPropertyListing(self,user_id):
        propertyEnt = PropertyListing()
        new_favourite_list = propertyEnt.viewPropertyListingbyAgentEmail(user_id)
        
        return new_favourite_list
        