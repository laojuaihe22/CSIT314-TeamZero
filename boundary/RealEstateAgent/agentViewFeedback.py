from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.viewRatingController import ViewRatingController
from controller.RealEstateAgent.viewReviewController import ViewReviewController

feedback_app = Blueprint('feedback_app', __name__)


@feedback_app.route('/agentViewFeedback', methods = ['GET'])
def feedback_app_page():
    
    if request.method == "GET":
        view_rating_controller = ViewRatingController()
        rating_list = view_rating_controller.viewRatingByagentId(session['id'])
        
        view_review_controller = ViewReviewController()
        review_list = view_review_controller.viewReviewByagentId(session['id'])
        
        if not rating_list and not review_list:
            return render_template('realEstateAgentViewFeedback.html', message="No Feedback!")
        
        feedback_list = combine_review_rating(rating_list, review_list)
        print(feedback_list)

        return render_template('realEstateAgentViewFeedback.html', feedback_listing=feedback_list)
    



def combine_review_rating(rating_list,review_list):
    
    combine_list = []
    
    for rating in rating_list:
        for review in review_list:
            if rating["receiver_id"] == review["receiver_id"]:
                combine_list.append({
                    "rating_value": rating["rating"],
                    "review_text": review["review"],
                    "sender_name": review["sender_name"]
                })
                
    
    return combine_list