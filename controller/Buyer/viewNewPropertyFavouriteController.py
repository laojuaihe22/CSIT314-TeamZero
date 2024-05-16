from entity.PropertyListing import PropertyListing

class ViewNewPropertyFavouriteController:
    
    
    def buyerFavouriteNewPropertyListing(self,user_email):
        propertyEnt = PropertyListing()
        new_favourite_list = propertyEnt.viewPropertyListingbyAgentEmail(user_email)
        
        
        
        