from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.createPropertyListingController import CreatePropertyListingController

create_property_listing_app = Blueprint('create_property_listing_app', __name__)



@create_property_listing_app.route('/createPropertyListing', methods = ['POST','GET'])
def create_property_listing_page():
     
    if request.method == "POST":
        agentID = session["user_email"]
        sellerID = request.form["sellerID"]
        property_address = request.form["address"]
        property_region = request.form["region"]
        property_price = int(request.form["price"])
        property_type = request.form["type"]
        property_description = request.form["description"]

        createPropertyListingController = CreatePropertyListingController()

        property_Created = createPropertyListingController.createPropertyListing(agentID, sellerID, property_address, property_region,  
                                                                                 property_price, property_type, property_description)
        
        if property_Created:
            flash('Successfully created', 'success')
            return render_template('realEstateAgentCreatePropertyListing.html')
        else:
            flash('Error: Invalid email address', 'error')
            return render_template('realEstateAgentCreatePropertyListing.html')
        
    return render_template('realEstateAgentCreatePropertyListing.html')