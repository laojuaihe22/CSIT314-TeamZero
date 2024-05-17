from entity.Rating import Rating

class SellerSubmitRatingController:
    def sellerSubmitRating(self,agent_email, sender_id, buyer_rating):
        
        rating_instance = Rating()
        submit_rating = rating_instance.submitRating(agent_email, sender_id, buyer_rating)
        
        return submit_rating