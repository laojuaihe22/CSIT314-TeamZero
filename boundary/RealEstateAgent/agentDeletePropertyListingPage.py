from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.deletePropertyListingController import DeletePropertyListingController


delete_property_listing_app = Blueprint('delete_property_listing_app', __name__)

@delete_property_listing_app.route('/deletePropertyListing', methods=['GET', 'POST'])
def delete_property_listing_page():
    if request.method == "POST":
        delete_property = request.form["address"]

        deletePropertyListingController = DeletePropertyListingController()
        property_deleted = deletePropertyListingController.deletePropertyListing(delete_property)

        if property_deleted:
            flash('Successfully deleted from property listing', 'success')
        else:
            flash('Failed to delete from property listing', 'error')
        
    return render_template('realEstateAgentDeletePropertyListing.html')