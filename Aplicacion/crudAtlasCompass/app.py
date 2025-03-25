from flask import Flask, render_template, request, redirect, url_for
from controladores.product_controller import ProductController
from controladores.client_controller import ClientController
from controladores.prov_controller import ProvController

app = Flask(__name__)

# Rutas de la aplicación
@app.route('/')
def home():
  return render_template('index.html')

@app.route("/productos")
def productos():
  return ProductController.view_products()

@app.route("/clientes")
def clientes():
  return ClientController.view_clients()

@app.route("/proveedores")
def proveedores():
  return ProvController.view_provs()

@app.route('/products', methods=['POST'])
def add_product():
  return ProductController.add_product()

@app.route('/delete_product/<string:product_name>')
def delete_product(product_name):
  return ProductController.delete_product(product_name)

@app.route('/edit/<string:product_name>', methods=['POST'])
def edit_product(product_name):
  return ProductController.edit_product(product_name)

@app.route('/clients', methods=['POST'])
def add_client():
  return ClientController.add_client()

@app.route('/delete_client/<string:client_name>')
def delete_client(client_name):
  return ClientController.delete_client(client_name)

@app.route('/editClient/<string:client_name>', methods=['POST'])
def edit_client(client_name):
  return ClientController.edit_client(client_name)

@app.route('/provs', methods=['POST'])
def add_prov():
  return ProvController.add_prov()

@app.route('/delete_prov/<string:prov_name>')
def delete_prov(prov_name):
  return ProvController.delete_prov(prov_name)

@app.route('/editProv/<string:prov_name>', methods=['POST'])
def edit_prov(prov_name):
  return ProvController.edit_prov(prov_name)

if __name__ == '__main__':
  app.run(debug=True, port=4000)
