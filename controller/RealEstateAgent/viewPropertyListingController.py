from entity.PropertyListing import PropertyListing

class ViewPropertyListingController():

    def viewPropertyListingbyAgentId(self, agentId):
        
        propertyListing = PropertyListing()
        property_list = propertyListing.viewPropertyListingbyAgentId(agentId)

        return property_list