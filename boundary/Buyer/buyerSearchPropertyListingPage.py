from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, flash
from controller.Buyer.searchPropertyController import BuyerSearchPropertyController

buyer_search_app = Blueprint('buyer_search_app', __name__)

@buyer_search_app.route('/buyer_search_property', methods=['POST','GET'])
def buyer_search_page():
    
    if request.method == 'POST':
        # Retrieve form values using request.form.get
        region = request.form.get('region')
        property_type = request.form.get('property_type')
        price_sort = request.form.get('price')
        status = request.form.get('status')

        buyer_search_property = BuyerSearchPropertyController()
        property_list = buyer_search_property.buyerSearchProperty(region,property_type,price_sort,status)
        
        if not property_list:
            return render_template('buyerSearchProperty.html', message="No properties found!")
        
        return render_template('buyerSearchProperty.html', property_list=property_list)
        
        
    return render_template('buyerSearchProperty.html')
    