from entity.Rating import Rating

class ViewRatingController:
    
    def viewRatingByagentEmail(self,email):
        agent_rating = Rating()
        feedback_list = agent_rating.viewRatingByagentEmail(email)
        
        return feedback_list