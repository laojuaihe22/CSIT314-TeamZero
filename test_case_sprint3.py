import unittest
from entity.PropertyListing import PropertyListing

class TestRealEstateMethods(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary objects or configurations before each test
        self.realestate = PropertyListing()  # Initialize your real estate class instance
        self.valid_agent = '6646edcc19880ce851a46cb1'
    def test_create_property_listing(self):
        
        
        result = self.realestate.createPropertyListing(agentId=self.valid_agent, sellerEmail="seller@gmail.com",
                                                        propertyName="Test Property", address="123 Test St",
                                                        region="North", price=100000, type="unsold",
                                                        description="Test Description", bedroom=3, bathroom=2)
        
        self.assertTrue(result)  # Check if the result is True, indicating successful creation

    def test_view_property_listing_by_agent_id(self):
        
        result = self.realestate.viewPropertyListingbyAgentId(agentId=self.valid_agent)
        self.assertTrue(result)  # Check if the result is not empty, indicating successful retrieval

    def test_update_property_listing(self):
        
        updated_property = self.realestate.updatePropertyListing(address="123 Test St", field="price", value=150000)
        self.assertTrue(updated_property)  

    def test_delete_property_listing(self):
        result = self.realestate.deletePropertyListing(address="123 Test St")
        self.assertTrue(result)  # Check if the result is True, indicating successful deletion

    def test_search_property_listing_by_agent_id(self):
        
        result = self.realestate.searchPropertyListingbyAgentId(agentID=self.valid_agent, filter_type="price", value="10000000")
        self.assertIsInstance(result, list)  

        


if __name__ == '__main__':
    unittest.main()
