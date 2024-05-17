from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Buyer.saveNewPropertyIntoFavouriteController import SaveNewPropertyController
from controller.Buyer.saveSoldPropertyIntoFavouriteController import SaveSoldPropertyController
from controller.Buyer.unsaveNewPropertyIntoFavouriteController import UnsaveNewPropertyController
from controller.Buyer.unsaveSoldPropertyIntoFavouriteController import UnsaveSoldPropertyController
from controller.Buyer.viewAllPropertyController import ViewAllPropertyListing
from controller.Buyer.viewNewPropertyFavouriteController import ViewNewPropertyFavouriteController
from controller.Buyer.viewSoldPropertyFavouriteController import ViewSoldPropertyFavouriteController
from bson import ObjectId

buyer_save_property_into_favourite_app = Blueprint('buyer_save_property_into_favourite_app', __name__)


@buyer_save_property_into_favourite_app.route('/saveNewProperty', methods=['POST', 'GET'])
def save_new_property_page():
    message=""
    
    if request.method == "POST":
        buyerID = session["id"]
        propertyID = request.form["propertyID"] 
        
        saveNewPropertyController = SaveNewPropertyController()
        is_inserted = saveNewPropertyController.saveNewProperty(buyerID, propertyID)
        
        # Check if shortListedIncreament is None
        if is_inserted :
           message = "Successfully added into your favourite list"
        else:
            message="Property you have already added."
            
    viewAllPropertyListing = ViewAllPropertyListing()
    property_list = viewAllPropertyListing.viewAllPropertyListing()
    
    return render_template('buyerViewAllProperty.html',property_list=property_list,message=message)

@buyer_save_property_into_favourite_app.route('/saveSoldProperty', methods=['POST', 'GET'])
def save_sold_property_page():
    
    message=" "
    if request.method == "POST":
        buyerID = session["id"]
        propertyID = request.form["propertyID"] 
        
        saveSoldPropertyController = SaveSoldPropertyController()
        is_inserted = saveSoldPropertyController.saveSoldProperty(buyerID, propertyID)
        
        
        if is_inserted :
           message = "Successfully added into your favourite list"
        else:
            message="Property you have already added."
            
    viewAllPropertyListing = ViewAllPropertyListing()
    property_list = viewAllPropertyListing.viewAllPropertyListing()
    
    return render_template('buyerViewAllProperty.html',property_list=property_list,message=message)

@buyer_save_property_into_favourite_app.route('/unsaveNewProperty', methods=['POST', 'GET'])
def unsave_new_property_page():
    message=""
    
    if request.method == "POST":
        buyerID = session["id"]
        propertyID = request.form["propertyID"] 
        
        unsaveNewPropertyController = UnsaveNewPropertyController()
        is_deleted = unsaveNewPropertyController.unsaveNewProperty(buyerID, propertyID)
        
        # Check if shortListedIncreament is None
        if is_deleted :
            message = "Successfully remove into your favourite list!"
            
    viewNewProperty = ViewNewPropertyFavouriteController()
    property_list = viewNewProperty.buyerViewFavouriteNewPropertyListing(session["id"])
    
    if property_list:
         return render_template('buyerViewNewProperty.html',property_list=property_list,message="message")
    else:
        return render_template('buyerViewNewProperty.html',message=message)

@buyer_save_property_into_favourite_app.route('/unsaveSoldProperty', methods=['POST', 'GET'])
def unsave_sold_property_page():
    message=""
    
    if request.method == "POST":
        buyerID = session["id"]
        propertyID = request.form["propertyID"] 
        
        unsaveSoldPropertyController = UnsaveSoldPropertyController()
        is_deleted = unsaveSoldPropertyController.unsaveSoldProperty(buyerID, propertyID)
        
        # Check if shortListedIncreament is None
        if is_deleted :
            message = "Successfully Remove!"
            
    viewSoldProperty = ViewSoldPropertyFavouriteController()
    property_list = viewSoldProperty.buyerViewFavouriteSoldPropertyListing(session["id"])
    
    if property_list:
         return render_template('buyerViewSoldProperty.html',property_list=property_list,message=message)
    else:
        return render_template('buyerViewSoldProperty.html',message=message)
    
    