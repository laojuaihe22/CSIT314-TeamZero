from entity.PropertyListing import PropertyListing

class SearchPropertyListingController():

    def searchPropertyListing(self, filter_type, value):

        propertyListing = PropertyListing()
        filtered_property_list = propertyListing.searchPropertyListing(filter_type, value)

        return filtered_property_list
