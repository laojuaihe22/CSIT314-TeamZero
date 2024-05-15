from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.updatePropertyListingController import UpdatePropertyListingController
from controller.RealEstateAgent.searchPropertyListingController import SearchPropertyListingController

update_property_listing_app = Blueprint('update_property_listing_app', __name__)

@update_property_listing_app.route('/updatePropertyListing', methods=['POST', 'GET'])
def update_property_listing_page():
    if request.method == 'POST':
        sellerEmail = request.form['sellerEmail']
        address = request.form['address']
        field = request.form['field']
        value = request.form['value']

        update_property_listing = UpdatePropertyListingController()

        if field == "price" or field == "bedroom" or field == "bathroom":
            try:
                value = int(value)  # Convert value to integer
                if value < 0:
                    return render_template('realEstateAgentUpdatePropertyListing.html', message=f"{field.capitalize()} must be a non-negative integer")
            except ValueError:
                return render_template('realEstateAgentUpdatePropertyListing.html', message=f"{field.capitalize()} must be an integer")
            
        elif field == "status":
            if value.lower() not in ["sold", "unsold"]:
                return render_template('realEstateAgentUpdatePropertyListing.html', message="Status can only be 'sold' or 'unsold'")
            value = value.lower()

        

        updated_property = update_property_listing.updatePropertyListing(address, field, value)
        
        if updated_property:
            return render_template('realEstateAgentUpdatePropertyListing.html', updated_property=updated_property, message="Property updated successfully!!")
        else:
            return render_template('realEstateAgentUpdatePropertyListing.html', updated_property=updated_property, message="Failed to update the property")
            
    return render_template('realEstateAgentUpdatePropertyListing.html')
