from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.viewRatingController import ViewRatingController

rating_app = Blueprint('rating_app', __name__)


@rating_app.route('/agentViewFeedback', methods = ['GET'])
def feedback_app():
    
    if request.method == "GET":
        view_rating_controller = ViewRatingController()
        rating_list = view_rating_controller.viewRatingByagentEmail(session['user_email'])
    
    print(rating_list)
    return render_template('realEstateAgentViewFeedback.html', rating_listing=rating_list)