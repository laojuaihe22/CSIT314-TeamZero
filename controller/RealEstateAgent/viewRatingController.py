from entity.Rating import Rating

class ViewRatingController:
    
    def viewRatingByagentId(self,agentId):
        agent_rating = Rating()
        feedback_list = agent_rating.viewRatingByagentId(agentId)
        
        return feedback_list