from flask import request, redirect, url_for, render_template
from modelos.client import Client
from controladores.db_controller import dbConnection

class ClientController:

    @staticmethod
    def view_clients():
        clients = dbConnection()['clients']
        clientsReceived = clients.find()
        return render_template("clientes.html", clients=clientsReceived)

    @staticmethod
    def add_client():
        fullName = request.form['fullName']
        email = request.form['email']
        direction = request.form['direction']
        note = request.form['note']
        clients = dbConnection()['clients']
        
        if fullName and email and direction and note:
            client = Client(fullName, email, direction, note)
            clients.insert_one(client.toDBCollection())
            return redirect(url_for('clientes'))
        else:
            return "Error: Faltan datos"

    @staticmethod
    def delete_client(client_name):
        clients = dbConnection()['clients']
        clients.delete_one({'fullName': client_name})
        return redirect(url_for('clientes'))

    @staticmethod
    def edit_client(client_name):
        fullName = request.form['fullName']
        email = request.form['email']
        direction = request.form['direction']
        note = request.form['note']
        clients = dbConnection()['clients']
        
        if fullName and email and direction and note:
            clients.update_one({'fullName': client_name}, {'$set': {'fullName': fullName, 'email': email, 'direction': direction, 'note': note}})
            return redirect(url_for('clientes'))
        else:
            return "Error: Faltan datos"
