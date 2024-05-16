from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Buyer.viewAllPropertyController import ViewAllPropertyListing
from controller.Buyer.viewNewPropertyFavouriteController import ViewNewPropertyFavouriteController
# from controller.Buyer.viewSoldPropertyFavouriteController import ViewSoldPropertyFavouriteController

buyer_view_property_listing_app = Blueprint('buyer_view_property_listing_app', __name__)

@buyer_view_property_listing_app.route('/viewAllPropertyListing', methods = ['GET'])
def buyer_view_all_property_listing_page():

    if request.method == "GET":
        viewAllPropertyListing = ViewAllPropertyListing()
        property_list = viewAllPropertyListing.viewAllPropertyListing()

        return render_template('buyerViewAllProperty.html', property_list = property_list)
    
    return redirect('/home')


@buyer_view_property_listing_app.route('/buyerFavouriteNewPropertyListing', methods = ['GET'])
def buyer_view_favourtie_new_property_listing_page():
    
    if request.method == "GET":
        viewNewProperty = ViewNewPropertyFavouriteController()
        property_list = viewNewProperty.buyerViewFavouriteNewPropertyListing(session["id"])
        return render_template('buyerViewNewProperty.html', property_list = property_list)
    
    return redirect('/home')

# @buyer_view_property_listing_app.route('/buyerFavouriteSoldPropertyListing', methods = ['GET'])
# def buyer_view_favourtie_sold_property_listing_page():
    
#     if request.method == "GET":
#         viewNewProperty = ViewNewPropertyFavouriteController()
#         property_list = viewNewProperty.buyerViewFavouriteNewPropertyListing(session["user_email"])
#         return render_template('buyerViewSoldProperty.html', property_list = property_list)
    
#     return redirect('/home')