from entity.PropertyListing import PropertyListing

class CreatePropertyListingController():

    def createPropertyListing(self, agentId, sellerEmail, propertyName, property_address,
                              property_region,  
                              property_price, property_type, property_description,
                              property_bedroom, property_bathroom):
        
        propertyListing = PropertyListing()
        property_doc = propertyListing.createPropertyListing(agentId, sellerEmail, propertyName, property_address,
                                                             property_region,  
                                                             property_price, property_type, property_description,
                                                             property_bedroom, property_bathroom)
        
        if property_doc:
            return True
        else:
            return False
        