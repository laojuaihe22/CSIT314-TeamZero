from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.viewPropertyListingController import ViewPropertyListingController

view_property_listing_app = Blueprint('view_property_listing_app', __name__)



@view_property_listing_app.route('/viewPropertyListingPage', methods = ['POST'])
def view_property_listing():
    if request.method == "GET":

        viewPropertyListingController = ViewPropertyListingController()
        property_list = viewPropertyListingController.viewPropertyListing()

        return render_template('viewPropertyListing.html',property_list=property_list)
    
    return redirect('/home')