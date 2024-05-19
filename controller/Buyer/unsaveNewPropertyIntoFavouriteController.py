from entity.NewFavouriteListing import NewFavourite


class UnsaveNewPropertyController:
    
    def unsaveNewProperty(self,buyerID, propertyID):
        new_favourite = NewFavourite()
        is_deleted = new_favourite.unsaveNewProperty(buyerID, propertyID)
        
        return is_deleted