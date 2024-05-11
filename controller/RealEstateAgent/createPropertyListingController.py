from entity.PropertyListing import PropertyListing

class CreatePropertyListingController():

    def createPropertyListing(self, agentID, sellerID, region, address, price, type, description):

        if not agentID or not sellerID or not region or not address or not price or not type or not description:
            return False 
        
        propertyListing = PropertyListing()
        property_doc = propertyListing.createPropertyListing(self, agentID, sellerID, region, address, price, type, description)
        
        if property_doc:
            return True
        else:
            return False
        