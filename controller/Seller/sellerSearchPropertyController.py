from entity.PropertyListing import PropertyListing

class SellerSearchPropertyController:
    
    def sellerSearchProperty(self,sellerId,region,property_type,price_sort,status):
        search_property = PropertyListing()
        
        property_list = search_property.seller_search_property(sellerId,region,property_type,price_sort,status)
        
        return property_list