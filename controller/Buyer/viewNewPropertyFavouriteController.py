from entity.NewFavouriteListing import NewFavourite

class ViewNewPropertyFavouriteController:
    
    
    def buyerViewFavouriteNewPropertyListing(self,buyer_id):
        new_favourite = NewFavourite()
        new_favourite_list = new_favourite.buyerViewFavouriteNewPropertyListing(buyer_id)
        
        return new_favourite_list
        