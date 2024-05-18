import unittest
from entity.NewFavouriteListing import NewFavourite
from entity.SoldFavouriteListing import SoldFavourite
from entity.PropertyListing import PropertyListing

from entity.Rating import Rating
from entity.Review import Review
from bson import ObjectId

class TestBuyerMethods(unittest.TestCase):
    
    def setUp(self):
        self.property = PropertyListing()
        self.newFavourite = NewFavourite()
        self.soldFavourite = SoldFavourite()
        self.review = Review()
        self.rating = Rating()
        
        self.valid_buyer = ObjectId('6646edd319880ce851a46cb4')
    
    def test_viewAllPropertyListing(self):
        # Call the method assuming there are properties available in the database
        result = self.property.viewAllPropertyListing()
        # Assertions
        self.assertTrue(result) 
        
    def test_saveNewProperty(self):
        # Test scenario where there is no existing document and both insert and update operations succeed
        
        existed_new_property = ObjectId('66485bd0cdfd8d1a0467ea77')
        
        # unsave before we proceed to test the save new property
        self.newFavourite.unsaveNewProperty(self.valid_buyer, existed_new_property)
        
        result = self.newFavourite.saveNewProperty(self.valid_buyer,existed_new_property)
        result_saved_again = self.newFavourite.saveNewProperty(self.valid_buyer,existed_new_property)
        
        self.assertTrue(result) 
        self.assertFalse(result_saved_again) 
        
        
    def test_buyerViewFavouriteNewPropertyListing(self):
        
        
        existing_result = self.newFavourite.buyerViewFavouriteNewPropertyListing(self.valid_buyer)
       
        non_existent_buyer_id = ObjectId("5546edd319880ce851a46cb4")  
        non_existent_result = self.newFavourite.buyerViewFavouriteNewPropertyListing(non_existent_buyer_id)

        # Assertions
        self.assertIsInstance(existing_result, list) 
        self.assertFalse(non_existent_result)
        
    def test_saveSoldProperty(self):
        
        existed_property = ObjectId('66485bdccdfd8d1a0467ea79')
        
        # unsave before we proceed to test the save new property
        self.soldFavourite.unsaveSoldProperty(self.valid_buyer, existed_property)
        
        result = self.soldFavourite.saveSoldProperty(self.valid_buyer,existed_property)
        result_saved_again = self.soldFavourite.saveSoldProperty(self.valid_buyer,existed_property)
        
        # Assertions
        self.assertTrue(result) 
        self.assertFalse(result_saved_again) 
        
        
    def test_buyerViewFavouriteSoldPropertyListing(self):
        # Test scenario where there are properties available for the buyer
        
        existing_result = self.soldFavourite.buyerViewFavouriteSoldPropertyListing(self.valid_buyer)

        # Test scenario where there are no properties available for the buyer
        non_existent_buyer_id = ObjectId("5546edd319880ce851a46cb4") 
        non_existent_result = self.soldFavourite.buyerViewFavouriteSoldPropertyListing(non_existent_buyer_id)

        # Assertions
        self.assertTrue(existing_result)  
        self.assertFalse(non_existent_result) 
    
    def test_buyer_search_property(self):
        region = "North"
        property_type = "Condo"
        price_sort = "asc"
        status = "unsold"

        result = self.property.buyer_search_property(region,property_type,price_sort,status)
        self.assertIsInstance(result, list)         
        
    def test_submitReview(self):
        
        review = "Hi this is review"
        agentemail = "rea@gmail.com"
        not_existed_agentemail = "notexisted@gmail.com"
        
        result = self.review.submitReview(agentemail,self.valid_buyer,review)
        agentemail_not_existed_result = self.review.submitReview(not_existed_agentemail,self.valid_buyer,review)
        
        self.assertTrue(result)
        self.assertFalse(agentemail_not_existed_result)
    
    def test_submitRating(self):
        
        rating = 3
        agentemail = "rea@gmail.com"
        not_existed_agentemail = "notexisted@gmail.com"
        
        result = self.rating.submitRating(agentemail,self.valid_buyer,rating)
        agentemail_not_existed_result = self.rating.submitRating(not_existed_agentemail,self.valid_buyer,rating)
        
        self.assertTrue(result)
        self.assertFalse(agentemail_not_existed_result)
        
if __name__ == '__main__':
    unittest.main()
