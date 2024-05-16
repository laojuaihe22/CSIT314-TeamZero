from entity.NewFavouriteListing import NewFavourite

class SaveNewPropertyController():

    def saveNewProperty(self, buyerID, propertyID):

        new_favourite = NewFavourite()

        is_inserted = new_favourite.saveNewProperty(buyerID, propertyID)
        
        return is_inserted
