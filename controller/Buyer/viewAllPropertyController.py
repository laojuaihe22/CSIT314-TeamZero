from entity.PropertyListing import PropertyListing

class ViewAllPropertyListing():

    def viewAllPropertyListing(self):
        
        propertyListing = PropertyListing()
        property_list = propertyListing.viewPropertyListing()

        return property_list

    