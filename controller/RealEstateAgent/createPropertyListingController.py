from entity.PropertyListing import PropertyListing

class CreatePropertyListingController():

    def createPropertyListing(self, agentID, sellerID, address, region, price, type, description):
        
        propertyListing = PropertyListing()
        property_doc = propertyListing.createPropertyListing(agentID, sellerID, address, region, price, type, description)
        
        if property_doc:
            return True
        else:
            return False
        