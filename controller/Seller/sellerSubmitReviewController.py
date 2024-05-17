from entity.Review import Review

class SellerSubmitReviewController:
    
    def sellerSubmitReview(self,agent_email, sender_id, buyer_rating):
        review_instances = Review()
        submit_rating = review_instances.submitReview(agent_email, sender_id, buyer_rating)
        
        return submit_rating