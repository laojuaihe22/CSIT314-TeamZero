from entity.SoldFavouriteListing import SoldFavourite

class ViewSoldPropertyFavouriteController:
    
    def buyerViewFavouriteSoldPropertyListing(self,buyer_id):
        
        sold_favourite = SoldFavourite()
        new_favourite_list = sold_favourite.buyerViewFavouriteSoldPropertyListing(buyer_id)
        
        return new_favourite_list