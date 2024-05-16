from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Buyer.saveNewPropertyIntoFavouriteController import SaveNewPropertyController
from controller.Buyer.viewAllPropertyController import ViewAllPropertyListing
from flask import jsonify

buyer_save_property_into_favourite_app = Blueprint('buyer_save_property_into_favourite_app', __name__)



@buyer_save_property_into_favourite_app.route('/saveNewProperty', methods=['POST', 'GET'])
def save_new_property_page():
    
    if request.method == "POST":
        buyerID = session["user_email"]
        propertyID = request.form["propertyID"]

        saveNewPropertyController = SaveNewPropertyController()
        shortListedIncreament = saveNewPropertyController.saveNewPropertyController(buyerID, propertyID)
        
        # Check if shortListedIncreament is None
        if shortListedIncreament :
            return jsonify({"message": "Saved to favourite", "success": True})
        else:
            return jsonify({"message": "Unable to save", "success": False})

    
    return render_template('buyerViewAllProperty.html')

