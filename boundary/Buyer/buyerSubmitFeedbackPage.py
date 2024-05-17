from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Buyer.submitRatingController import SubmitRatingController
from controller.Buyer.submitReviewController import SubmitReviewController

submit_feedback_app = Blueprint('submit_feedback_app', __name__)

@submit_feedback_app.route('/submitFeedback', methods=['GET', 'POST'])
def buyer_Submit_Feedback_page():
    if request.method == "POST":
       
        agent_email = request.form["email"]
        buyer_review = request.form["review"]
        buyer_rating = request.form["rating"]
        sender_id = session["id"]  # Ensure this is a valid ObjectId string

        
        submitRatingController = SubmitRatingController()
        submitReviewController = SubmitReviewController()

        submitRating = submitRatingController.buyerSubmitRating(agent_email, sender_id, buyer_rating)
        submitReview = submitReviewController.buyerSubmitReview(agent_email, sender_id, buyer_review)

        if submitRating and submitReview:
            
            return render_template('buyerSubmitFeedback.html', message = 'Feedback submitted successfully!')
        else:
           
            return render_template('buyerSubmitFeedback.html', message = 'Agent email not existed. Please try again.')
        

    return render_template('buyerSubmitFeedback.html')
