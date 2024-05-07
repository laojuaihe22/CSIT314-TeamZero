from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.createPropertyListingController import CreatePropertyListingController

create_property_listing_app = Blueprint('create_property_listing_app', __name__)

@create_property_listing_app.route('/createPropertyListingPage', methods = ['POST'])
def create_property_listing_page():

    return render_template('createPropertyListing.html')

@create_property_listing_app.route('/createPropertyListing', methods = ['POST'])
def create_property_listing():

    if request.method == "POST":
        agentID = request.form["agentID"]
        property_region = request.form["region"]
        property_address = request.form["address"]
        property_price = request.form["price"]
        property_type = request.form["type"]
        property_description = request.form["description"]

        createPropertyListingController = CreatePropertyListingController()

        property_Created = createPropertyListingController.createPropertyListing(agentID, property_region, property_address, 
                                                                                 property_price, property_type, property_description)
        
        if property_Created:
            flash(f'Successfully added to property listing', 'success')
        else:
            flash('Failed to add to property listing', 'error')
        
    return redirect('/createPropertyListingPage')