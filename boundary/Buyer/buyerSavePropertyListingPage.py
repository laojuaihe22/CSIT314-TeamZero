from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Buyer.saveNewPropertyIntoFavouriteController import SaveNewPropertyController
from controller.Buyer.viewAllPropertyController import ViewAllPropertyListing
from bson import ObjectId

buyer_save_property_into_favourite_app = Blueprint('buyer_save_property_into_favourite_app', __name__)


@buyer_save_property_into_favourite_app.route('/saveNewProperty', methods=['POST', 'GET'])
def save_new_property_page():
    message=""
    
    if request.method == "POST":
        buyerID = session["id"]
        propertyID = request.form["propertyID"] 
        saveNewPropertyController = SaveNewPropertyController()
        shortListedIncreament = saveNewPropertyController.saveNewPropertyController(buyerID, propertyID)
        
        
        # Check if shortListedIncreament is None
        if shortListedIncreament :
           message = "Successfully added into your favourite list"
        else:
            message="Property listing already added."
            
    viewAllPropertyListing = ViewAllPropertyListing()
    property_list = viewAllPropertyListing.viewAllPropertyListing()
    return render_template('buyerViewAllProperty.html',property_list=property_list,message=message)

