from entity.PropertyListing import PropertyListing

class BuyerSearchPropertyController():
    
    def buyerSearchProperty(self,region,property_type,price_sort,status):
        search_property = PropertyListing()
        property_list = search_property.buyer_search_property(region,property_type,price_sort,status)
        

        return property_list
