from entity.Review import Review

class ViewReviewController:
    
    def viewReviewByagentId(self,agentId):
        agent_review = Review()
        review_list = agent_review.viewReviewByagentId(agentId)
        
        return review_list