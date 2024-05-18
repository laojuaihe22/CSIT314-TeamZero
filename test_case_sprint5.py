from entity.Rating import Rating
from entity.Review import Review
import unittest
from entity.PropertyListing import PropertyListing
from bson import ObjectId


class TestSellerMethods(unittest.TestCase):
    
    def setUp(self):
        # Initialize an instance of YourClass
        self.propertyList = PropertyListing()
        self.review = Review()
        self.rating = Rating()
        self.valid_seller = ObjectId('6646edda19880ce851a46cb7')
        
    def test_viewPropertyListingbySellerId(self):
        result = self.propertyList.viewPropertyListingbySellerId(self.valid_seller)
        self.assertIsInstance(result, list) 
    
    def test_submitReview(self):
        
        review = "Hi this is seller review "
        agentemail = "rea@gmail.com"
        not_existed_agentemail = "notexisted@gmail.com"
        
        result = self.review.submitReview(agentemail,self.valid_seller,review)
        agentemail_not_existed_result = self.review.submitReview(not_existed_agentemail,self.valid_seller,review)
        
        self.assertTrue(result)
        self.assertFalse(agentemail_not_existed_result)
    
    def test_submitRating(self):
        
        rating = 3
        agentemail = "rea@gmail.com"
        not_existed_agentemail = "notexisted@gmail.com"
        
        result = self.rating.submitRating(agentemail,self.valid_seller,rating)
        agentemail_not_existed_result = self.rating.submitRating(not_existed_agentemail,self.valid_seller,rating)
        
        self.assertTrue(result)
        self.assertFalse(agentemail_not_existed_result)
        


if __name__ == '__main__':
    unittest.main()