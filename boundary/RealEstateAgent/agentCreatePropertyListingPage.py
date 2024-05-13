from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.createPropertyListingController import CreatePropertyListingController

create_property_listing_app = Blueprint('create_property_listing_app', __name__)



@create_property_listing_app.route('/createPropertyListing', methods = ['POST','GET'])
def create_property_listing_page():
     
    if request.method == "POST":
        agentID = session["email"]
        sellerID = request.form["sellerID"]
        property_region = request.form["region"]
        property_address = request.form["address"]
        property_price = request.form["price"]
        property_type = request.form["type"]
        property_description = request.form["description"]

        createPropertyListingController = CreatePropertyListingController()

        property_Created = createPropertyListingController.createPropertyListing(agentID, sellerID, property_region, property_address, 
                                                                                 property_price, property_type, property_description)
        
        if property_Created:
            flash(f'Successfully added to property listing', 'success')
        else:
            flash('Failed to add to property listing', 'error')
        
    return render_template('createListing.html')