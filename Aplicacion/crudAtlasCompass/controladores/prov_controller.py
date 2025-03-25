from flask import request, redirect, url_for, render_template
from modelos.prov import Prov
from controladores.db_controller import dbConnection

class ProvController:
    @staticmethod
    def view_provs():
        provs = dbConnection()['provs']
        provsReceived = provs.find()
        return render_template("proveedores.html", provs=provsReceived)

    @staticmethod
    def add_prov():
        namePro = request.form['namePro']
        email = request.form['email']
        direction = request.form['direction']
        phone = request.form['phone']
        provs = dbConnection()['provs']
        
        if namePro and email and direction and phone:
            prov = Prov(namePro, email, direction, phone)
            provs.insert_one(prov.toDBCollection())
            return redirect(url_for('proveedores'))
        else:
            return "Error: Faltan datos"

    @staticmethod
    def delete_prov(prov_name):
        provs = dbConnection()['provs']
        provs.delete_one({'namePro': prov_name})
        return redirect(url_for('proveedores'))

    @staticmethod
    def edit_prov(prov_name):
        namePro = request.form['namePro']
        email = request.form['email']
        direction = request.form['direction']
        phone = request.form['phone']
        provs = dbConnection()['provs']
        
        if namePro and email and direction and phone:
            provs.update_one({'namePro': prov_name}, {'$set': {'namePro': namePro, 'email': email, 'direction': direction, 'phone': phone}})
            return redirect(url_for('proveedores'))
        else:
            return "Error: Faltan datos"
