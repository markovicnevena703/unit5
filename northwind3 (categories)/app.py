from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def suppliers():
    suppliers = database.get_all_suppliers()
    return render_template('index.html', suppliers=suppliers)
@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = database.get_supplier_products(supplier_id)
    CompanyName = database.get_supplier_name(supplier_id)
    return render_template('products.html', products=products, CompanyName=CompanyName)


@app.route("/categories")
def categories():
    categories = database.get_categories()
    return render_template('categories.html', categories=categories)