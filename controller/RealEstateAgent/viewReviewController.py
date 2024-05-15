from entity.Review import Review

class ViewReviewController:
    
    def viewReviewByagentEmail(self,email):
        agent_review = Review()
        review_list = agent_review.viewReviewByagentEmail(email)
        
        return review_list