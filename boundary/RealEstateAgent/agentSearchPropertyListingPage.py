from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.SystemAdmin.searchUserProfileController import SearchUserProfileController


search_property_listing_app = Blueprint('search_property_listing_app', __name__)

@search_property_listing_app.route('/searchUserProfilePage', methods=['GET', 'POST'])
def search_property_listing_page():

    return render_template('searchPropertyListing.html')

@search_property_listing_app.route('/searchUserProfile', methods=['GET', 'POST'])
def search_property_listing():
    if request.method == "POST":
        filter_type = request.form['filter']
        filter_value = request.form['value']

        searchUserProfileController = SearchUserProfileController()
        property_list = searchUserProfileController.searchUserProfile(filter_type, filter_value)

        if property_list:
            flash('Results found', 'success')
            return render_template('/searchPropertyListing.html', property_list=property_list)
        else:
            flash('No similar result', 'error')

    return render_template('/searchPropertyListing.html', property_list=None)        