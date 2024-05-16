from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.RealEstateAgent.searchPropertyListingController import SearchPropertyListingController


search_property_listing_app = Blueprint('search_property_listing_app', __name__)



@search_property_listing_app.route('/searchPropertyListing', methods=['GET', 'POST'])
def search_property_listing_page():
    if request.method == "POST":
        filter_type = request.form['filter']
        filter_value = request.form['value']
        


        searchPropertyListingController = SearchPropertyListingController()
        property_list = searchPropertyListingController.searchPropertyListingbyAgentId(session['id'],filter_type, filter_value)

        if property_list:
            return render_template('/realEstateAgentSearchPropertyListing.html', property_list=property_list)
        else:
            flash('No similar result', 'error')

    return render_template('/realEstateAgentSearchPropertyListing.html', property_list=None)        