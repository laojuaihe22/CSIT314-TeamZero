from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.viewPropertyListingController import ViewPropertyListingController

view_property_listing_app = Blueprint('view_property_listing_app', __name__)



@view_property_listing_app.route('/viewPropertyListingPage', methods = ['POST', 'GET'])
def view_property_listing_page():
    if request.method == "GET":
        viewPropertyListingController = ViewPropertyListingController()
        property_list = viewPropertyListingController.viewPropertyListingbyId(session["id"])
        
        if property_list:
            return render_template('realEstateAgentViewPropertyListing.html',property_list=property_list)
        else:
            return render_template('realEstateAgentViewPropertyListing.html',message="No Property Listing existed in your account!")
    
    return redirect('/home')