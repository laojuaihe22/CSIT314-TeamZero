from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Seller.sellerViewPropertyController import SellerViewPropertyController

seller_view_property_listing_app = Blueprint('seller_view_property_listing_app', __name__)

@seller_view_property_listing_app.route('/sellerViewPropertyListing', methods = ['GET'])
def seller_view_property_listing_page():

    if request.method == "GET":
        seller_view_property_controller = SellerViewPropertyController()
        property_list = seller_view_property_controller.viewPropertyListingbySellerId(session['id'])
        
        if property_list:
            return render_template('sellerViewProperty.html',property_list=property_list)
        else:
            return render_template('sellerViewProperty.html',message="No Property Listing existed in your account!")
    
    return redirect('/home')
