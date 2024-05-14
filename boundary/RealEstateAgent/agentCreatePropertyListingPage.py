from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.createPropertyListingController import CreatePropertyListingController

create_property_listing_app = Blueprint('create_property_listing_app', __name__)



@create_property_listing_app.route('/createPropertyListing', methods = ['POST','GET'])
def create_property_listing_page():
     
    if request.method == "POST":
        agentEmail = session["user_email"]
        sellerEmail = request.form["sellerEmail"]
        sellerName = request.form["sellerName"]
        property_address = request.form["address"]
        property_region = request.form["region"]
        property_price = int(request.form["price"])
        property_type = request.form["type"]
        property_description = request.form["description"]
        property_bedroom = request.form["bedroom"]
        property_bathroom = request.form["bathroom"]
        
        createPropertyListingController = CreatePropertyListingController()

        property_Created = createPropertyListingController.createPropertyListing(agentEmail, sellerEmail, sellerName, property_address,
                                                                                 property_region,  
                                                                                 property_price, property_type, property_description,
                                                                                 property_bedroom, property_bathroom)                                                                                
        
        if property_Created:
            
            return render_template('realEstateAgentCreatePropertyListing.html', message = 'Successfully created')
        else:
            return render_template('realEstateAgentCreatePropertyListing.html', message = 'Failed to create')
        
    return render_template('realEstateAgentCreatePropertyListing.html')