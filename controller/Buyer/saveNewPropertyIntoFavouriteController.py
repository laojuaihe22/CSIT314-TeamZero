from entity.PropertyListing import PropertyListing

class SaveNewPropertyController():

    def saveNewPropertyController(self, buyerID, propertyID):

        propertyListing = PropertyListing()

        appendFavourite = propertyListing.appendFavouriteList(buyerID, propertyID)
        
        if appendFavourite: 
            shortListedIncreament = propertyListing.shortlistedIncrement(propertyID)

            return shortListedIncreament
