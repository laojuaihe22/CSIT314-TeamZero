from entity.Favourite import Favourite

class ViewNewPropertyFavouriteController:
    
    
    def buyerViewFavouriteNewPropertyListing(self,buyer_id):
        favourite = Favourite()
        new_favourite_list = favourite.buyerViewFavouritePropertyListing(buyer_id)
        
        return new_favourite_list
        