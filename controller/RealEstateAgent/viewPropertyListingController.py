from entity.PropertyListing import PropertyListing

class ViewPropertyListingController():

    def viewPropertyListingbyAgentEmail(self, agentEmail):
        
        propertyListing = PropertyListing()
        property_list = propertyListing.viewPropertyListingbyAgentEmail(agentEmail)

        return property_list