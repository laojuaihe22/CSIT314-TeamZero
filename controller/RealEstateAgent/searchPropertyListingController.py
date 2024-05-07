from entity.PropertyListing import PropertyListing

class SearchPropertyListingController():

    def searchPropertyListing(self, filter, value):

        propertyListing = PropertyListing()
        filtered_property_list = propertyListing.searchPropertyListing(filter, value)

        return filtered_property_list
