from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash

buyer_view_property_listing_app = Blueprint('buyer_view_property_listing_app', __name__)



@buyer_view_property_listing_app.route('/viewAllPropertyListing', methods = ['GET'])
def buyer_view_all_property_listing_page():
    
    if request.method == "GET":
        return render_template('buyerViewAllProperty.html')
    
    return redirect('/home')




