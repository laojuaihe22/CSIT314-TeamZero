from entity.SoldFavouriteListing import SoldFavourite

class SaveSoldPropertyController():

    def saveSoldProperty(self, buyerID, propertyID):

        sold_favourite = SoldFavourite()

        is_inserted = sold_favourite.saveSoldProperty(buyerID, propertyID)
        
        return is_inserted
