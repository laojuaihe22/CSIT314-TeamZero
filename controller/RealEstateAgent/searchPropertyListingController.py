from entity.PropertyListing import PropertyListing

class SearchPropertyListingController():

    def searchPropertyListingbyAgentId(self, agentID, filter_type, value):

        propertyListing = PropertyListing()
        filtered_property_list = propertyListing.searchPropertyListingbyAgentId(agentID, filter_type, value)

        return filtered_property_list
