from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.deletePropertyListingController import DeletePropertyListingController


delete_property_listing_app = Blueprint('delete_property_listing_app', __name__)

@delete_property_listing_app.route('/deletePropertyListingPage', methods=['GET', 'POST'])
def delete_property_listing_page():
    return render_template('deletePropertyListing.html')

@delete_property_listing_app.route('/deletePropertyListing', methods=['GET', 'POST'])
def delete_property_listing():
    if request.method == "POST":
        delete_user = request.form["address"]

        deletePropertyListingController = DeletePropertyListingController()
        user_deleted = deletePropertyListingController.deletePropertyListing(delete_user)

        if user_deleted:
            flash('Successfully deleted from property listing', 'success')
        else:
            flash('Failed to delete from property listing', 'error')
        
    return redirect('/home')