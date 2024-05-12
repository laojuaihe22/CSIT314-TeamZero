from entity.PropertyListing import PropertyListing

class CreatePropertyListingController():

    def createPropertyListing(self, agentID, sellerID, region, address, price, type, description):
        
        propertyListing = PropertyListing()
        property_doc = propertyListing.createPropertyListing(self, agentID, sellerID, region, address, price, type, description)
        
        if property_doc:
            return True
        else:
            return False
        