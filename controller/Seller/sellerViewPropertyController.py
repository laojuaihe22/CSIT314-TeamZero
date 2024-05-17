from entity.PropertyListing import PropertyListing

class SellerViewPropertyController:
    def viewPropertyListingbySellerId(self, seller_id):
        
        propertyListing = PropertyListing()
        property_listing = propertyListing.viewPropertyListingbySellerId(seller_id)
        
        return property_listing