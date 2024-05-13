from entity.PropertyListing import PropertyListing

class UpdatePropertyListingController():

    def updatePropertyListing(self, address, field, value):

        propertyListing = PropertyListing()
        updated_property = propertyListing.updatePropertyListing(address, field, value)

        return updated_property