from entity.PropertyListing import PropertyListing

class ViewNewPropertyFavouriteController:
    
    
    def buyerViewFavouriteNewPropertyListing(self,buyer_id):
        propertyEnt = PropertyListing()
        new_favourite_list = propertyEnt.buyerViewFavouritePropertyListing(buyer_id)
        
        return new_favourite_list
        