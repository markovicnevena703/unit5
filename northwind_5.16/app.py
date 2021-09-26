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


@app.route("/categories/<int:category_id>")
def categories(category_id):
    categories = database.get_categories(category_id)
    CategoryName=database.get_category_name(category_id)
    return render_template('categories.html', categories=categories, CategoryName=CategoryName)

@app.route("/categories/")
def categories_basic():
    all_categories = database.get_all_categories()
    return render_template('categories_basic.html', all_categories=all_categories)