from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Seller.sellerSearchPropertyController import SellerSearchPropertyController

seller_search_app = Blueprint('seller_search_app', __name__)

@seller_search_app.route('/seller_search_property', methods=['POST','GET'])
def seller_search_property_page():
    if request.method == 'POST':
    # Retrieve form values using request.form.get
        region = request.form.get('region')
        property_type = request.form.get('property_type')
        price_sort = request.form.get('price')
        status = request.form.get('status')
        
        seller_search_property_controller = SellerSearchPropertyController()
        property_list = seller_search_property_controller.sellerSearchProperty(session['id'],region,property_type,price_sort,status)
        
        if not property_list:
            return render_template('sellerSearchProperty.html', message="No properties found!")
        
        return render_template('sellerSearchProperty.html', property_list=property_list)
        
    return render_template('sellerSearchProperty.html')
    
    