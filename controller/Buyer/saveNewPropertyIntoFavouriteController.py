from entity.Favourite import Favourite

class SaveNewPropertyController():

    def saveNewPropertyController(self, buyerID, propertyID):

        favourite = Favourite()

        appendFavourite = favourite.appendFavouriteList(buyerID, propertyID)
        
        if appendFavourite: 
            shortListedIncreament = favourite.shortlistedIncrement(propertyID)

            return shortListedIncreament
