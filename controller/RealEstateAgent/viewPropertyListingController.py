from entity.PropertyListing import PropertyListing

class ViewPropertyListingController():

    def viewPropertyListing(self):
        propertyListing = PropertyListing()
        property_list = propertyListing.viewPropertyListing(self)


        return property_list