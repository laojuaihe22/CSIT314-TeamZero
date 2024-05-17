from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Seller.sellerSubmitRatingController import SellerSubmitRatingController
from controller.Seller.sellerSubmitReviewController import SellerSubmitReviewController

seller_submit_feedback_app = Blueprint('seller_submit_feedback_app', __name__)

@seller_submit_feedback_app.route('/seller_submit_feedback', methods=['GET', 'POST'])
def seller_submit_feedback_page():
    
    
    if request.method == "POST":
       
        agent_email = request.form["email"]
        buyer_review = request.form["review"]
        buyer_rating = request.form["rating"]
        sender_id = session["id"]  # Ensure this is a valid ObjectId string

        
        submitRatingController = SellerSubmitRatingController()
        submitReviewController = SellerSubmitReviewController()

        submitRating = submitRatingController.sellerSubmitRating(agent_email, sender_id, buyer_rating)
        submitReview = submitReviewController.sellerSubmitReview(agent_email, sender_id, buyer_review)

        if submitRating and submitReview:
            
            return render_template('sellerSubmitFeedback.html', message = 'Feedback submitted successfully!')
        else:
           
            return render_template('sellerSubmitFeedback.html', message = 'Agent email not existed. Please try again.')
        

    return render_template('sellerSubmitFeedback.html')
