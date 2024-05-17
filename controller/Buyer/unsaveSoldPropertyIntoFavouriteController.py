from entity.SoldFavouriteListing import SoldFavourite


class UnsaveSoldPropertyController:
    
    def unsaveSoldProperty(self,buyerID, propertyID):
        
        sold_favourite = SoldFavourite()
        is_deleted = sold_favourite.unsaveSoldProperty(buyerID, propertyID)
        
        return is_deleted