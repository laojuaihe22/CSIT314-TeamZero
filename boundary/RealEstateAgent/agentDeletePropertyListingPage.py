from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.deletePropertyListingController import DeletePropertyListingController
from controller.RealEstateAgent.viewPropertyListingController import ViewPropertyListingController


delete_property_listing_app = Blueprint('delete_property_listing_app', __name__)

@delete_property_listing_app.route('/deletePropertyListing', methods=['GET', 'POST'])
def delete_property_listing_page():
    
    message = ""
    
    if request.method == "POST":
        delete_property = request.form["address"]

        deletePropertyListingController = DeletePropertyListingController()
        property_deleted = deletePropertyListingController.deletePropertyListing(delete_property)

        if property_deleted:
            message = "Sucessfully Deleted Property!"
        else:
            message = "Failed to delete from property listing"
            
    viewPropertyListingController = ViewPropertyListingController()
    property_list = viewPropertyListingController.viewPropertyListingbyAgentId(session["id"])  
    
    if property_list:
        return render_template('realEstateAgentDeletePropertyListing.html',message=message,propertyListing=property_list)
    else:
        return render_template('realEstateAgentDeletePropertyListing.html',message="No Property Listing can be displayed!")