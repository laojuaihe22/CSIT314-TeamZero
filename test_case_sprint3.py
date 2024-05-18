import unittest
from entity.PropertyListing import PropertyListing
from entity.Rating import Rating
from entity.Review import Review

class TestRealEstateMethods(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary objects or configurations before each test
        self.realestate = PropertyListing()  # Initialize your real estate class instance
        self.rating = Rating()
        self.review = Review()
        
        self.valid_agent = '6646edcc19880ce851a46cb1'
        self.not_valid_seller_email = "nonexistent@example.com"
    def test_create_property_listing(self):
        
        
        result = self.realestate.createPropertyListing(agentId=self.valid_agent, sellerEmail="seller@gmail.com",
                                                        propertyName="Test Property", address="123 Test St",
                                                        region="North", price=100000, type="unsold",
                                                        description="Test Description", bedroom=3, bathroom=2)
        
        self.assertTrue(result)  # Check if the result is True, indicating successful creation
        
        
        false_result = self.realestate.createPropertyListing(agentId=self.valid_agent, sellerEmail=self.not_valid_seller_email,
                                                        propertyName="Test Property", address="123 Test St",
                                                        region="North", price=100000, type="unsold",
                                                        description="Test Description", bedroom=3, bathroom=2)
        self.assertFalse(false_result)

    def test_view_property_listing_by_agent_id(self):
        
        result = self.realestate.viewPropertyListingbyAgentId(agentId=self.valid_agent)
        self.assertIsInstance(result, list)  # Check if the result is not empty, indicating successful retrieval

    def test_update_property_listing(self):
        
        updated_property = self.realestate.updatePropertyListing(address="123 Test St", field="price", value=150000)
        self.assertTrue(updated_property)  
        
        updated_not_valid_property = self.realestate.updatePropertyListing(address="Not valid address", field="price", value=150000)
        self.assertFalse(updated_not_valid_property) 
        
    def test_search_property_listing_by_agent_id(self):
        
        result = self.realestate.searchPropertyListingbyAgentId(agentID=self.valid_agent, filter_type="price", value="10000000")
        self.assertIsInstance(result, list) 


    def test_delete_property_listing(self):
        result = self.realestate.deletePropertyListing(address="123 Test St")
        self.assertTrue(result)  # Check if the result is True, indicating successful deletion
        
        false_result = self.realestate.deletePropertyListing(address="not valid address")
        self.assertFalse(false_result)
        
    def test_viewRatingByagentId(self):
        # Test with an existing agent id
        
        existing_result = self.rating.viewRatingByagentId(self.valid_agent)

        # Test with a non-existent agent id
        non_existent_agent_id = "5546edcc19880ce851a46cb1"
        non_existent_result = self.rating.viewRatingByagentId(non_existent_agent_id)

        # Assertions
        self.assertTrue(existing_result)  # Assuming result is expected to be truthy for an existing agent
        self.assertFalse(non_existent_result)  # Assuming result is expected to be falsy for a non-existent agent

    def test_viewReviewByagentId(self):
        
        existing_result = self.review.viewReviewByagentId(self.valid_agent)

        # Test with a non-existent agent id
        non_existent_agent_id = "5546edcc19880ce851a46cb1"
        non_existent_result = self.review.viewReviewByagentId(non_existent_agent_id)

        # Assertions
        self.assertTrue(existing_result)  # Assuming result is expected to be truthy for an existing agent
        self.assertFalse(non_existent_result)
        


if __name__ == '__main__':
    unittest.main()
