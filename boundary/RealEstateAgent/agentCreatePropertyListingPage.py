from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.createPropertyListingController import CreatePropertyListingController

create_property_listing_app = Blueprint('create_property_listing_app', __name__)



@create_property_listing_app.route('/createPropertyListing', methods=['POST', 'GET'])
def create_property_listing_page():
    if request.method == "POST":
        try:
            property_price = int(request.form["price"])
            if property_price < 0:
                return render_template('realEstateAgentCreatePropertyListing.html', message="Price must be a non-negative integer")

            property_bedroom = int(request.form["bedroom"])
            if property_bedroom < 0:
                return render_template('realEstateAgentCreatePropertyListing.html', message="Number of bedroom must be a non-negative integer")

            property_bathroom = int(request.form["bathroom"])
            if property_bathroom < 0:
                return render_template('realEstateAgentCreatePropertyListing.html', message="Number of bathroom must be a non-negative integer")

        except ValueError as e:
            field_name = str(e).split("'")[1]
            if field_name == "price":
                return render_template('realEstateAgentCreatePropertyListing.html', message="Price must be an integer")
            elif field_name == "bedroom":
                return render_template('realEstateAgentCreatePropertyListing.html', message="Number of bedroom must be an integer")
            elif field_name == "bathroom":
                return render_template('realEstateAgentCreatePropertyListing.html', message="Number of bathroom must be an integer")

        agentId = session["id"]
        sellerEmail = request.form["sellerEmail"]
        propertyName = request.form["propertyName"]
        property_address = request.form["address"]
        property_region = request.form["region"]
        property_type = request.form["type"]
        property_description = request.form["description"]

        createPropertyListingController = CreatePropertyListingController()
        property_Created = createPropertyListingController.createPropertyListing(
            agentId, sellerEmail, propertyName, property_address,
            property_region, property_price, property_type, property_description,
            property_bedroom, property_bathroom
        )

        if property_Created:
            return render_template('realEstateAgentCreatePropertyListing.html', message='Successfully created!')
        else:
            return render_template('realEstateAgentCreatePropertyListing.html', message='Seller Email not existed!')

    return render_template('realEstateAgentCreatePropertyListing.html')
