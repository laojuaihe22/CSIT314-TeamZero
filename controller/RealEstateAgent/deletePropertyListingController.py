from entity.PropertyListing import PropertyListing

class DeletePropertyListingController():
    def deletePropertyListing(address):

        if not address:
            return False 

        propertyListing = PropertyListing()
        property_deleted = propertyListing.deletePropertyListing(address)

        if property_deleted:
            return True
        else: 
            return False