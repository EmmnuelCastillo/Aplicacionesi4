from flask import request, redirect, url_for, render_template
from modelos.product import Product
from controladores.db_controller import dbConnection

class ProductController:

    @staticmethod
    def view_products():
        products = dbConnection()['products']
        productsReceived = products.find()
        return render_template("productos.html", products=productsReceived)

    @staticmethod
    def add_product():
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        products = dbConnection()['products']
        
        if name and price and quantity:
            product = Product(name, price, quantity)
            products.insert_one(product.toDBCollection())
            return redirect(url_for('productos'))
        else:
            return "Error: Faltan datos"

    @staticmethod
    def delete_product(product_name):
        products = dbConnection()['products']
        products.delete_one({'name': product_name})
        return redirect(url_for('productos'))

    @staticmethod
    def edit_product(product_name):
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        products = dbConnection()['products']
        
        if name and price and quantity:
            products.update_one({'name': product_name}, {'$set': {'name': name, 'price': price, 'quantity': quantity}})
            return redirect(url_for('productos'))
        else:
            return "Error: Faltan datos"
