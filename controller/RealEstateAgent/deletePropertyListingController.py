from entity.PropertyListing import PropertyListing

class DeletePropertyListingController():
    def deletePropertyListing(self, address):

        propertyListing = PropertyListing()
        property_deleted = propertyListing.deletePropertyListing(address)

        if property_deleted:
            return True
        else: 
            return False