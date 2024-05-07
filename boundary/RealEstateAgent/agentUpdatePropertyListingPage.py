from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.updatePropertyListingController import UpdatePropertyListingController

update_property_listing_app = Blueprint('update_property_listing_app', __name__)

@update_property_listing_app.route('/updatePropertyListingPage')
def update_property_listing_page():
    
    return render_template('updatePropertyListing.html')

@update_property_listing_app.route('/updatePropertyListing', methods = ['POST'])
def update_property_listing():
    if request.method == 'POST':

        address = request.form['address']
        field = request.form['field']
        value = request.form['value']

        update_property_listing = UpdatePropertyListingController()
        updated_property = update_property_listing.updatePropertyListing(address, field, value)
        
        if updated_property:
            flash(f'Property successfully updated', 'success')
            return render_template('updatePropertyListing.html', updated_property=updated_property)
        else:
            flash('Failed to update the property', 'error')
