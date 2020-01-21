from flask import Flask, render_template, request, redirect, url_for
from Forms import ProductCreate
import shelve
from product import Product
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOADED_PHOTOS_DEST'] = ".\\static\img"


@app.route('/')
def home():
    products = []
    with shelve.open("data", "r") as db:
        products = db["product"]
    return render_template("home.html", products=products)


@app.route('/search')
def search():
    search_products = []
    query = request.args.get("search")
    products = []
    with shelve.open("data", "r") as db:
        products = db["product"]
    for product in products:
        if query.upper() in product.get_title().upper():
            search_products.append(product)
    return render_template("search.html", products=search_products)


@app.route('/products/<string:id>/')
def product_detail(id):
    with shelve.open("data", "r") as db:
        products = db["product"]
    for product in products:
        if product.get_id() == id:
            return render_template("product_details.html", product=product)


@app.route("/createProduct/", methods=["POST", "GET"])
def create_product():
    form = ProductCreate(request.form)
    if request.method == "GET":
        return render_template("createProduct.html", form=form)
    elif request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename))
        image_url = "/static/img/" + filename
        productList = []
        db = shelve.open('data', 'c')
        try:
            productList = db['product']
        except:
            print("Error in retrieving Users from storage.db.")
        product = Product(str(form.id.data), form.title.data, form.description.data,
                          form.stock.data, form.costprice.data, form.retailprice.data, image_url)
        productList.append(product)
        db['product'] = productList
        db.close()
        return redirect("/retrieveProduct")


@app.route('/retrieveProduct')
def retrieveProduct():
    productList = []
    db = shelve.open('data', 'r')
    productList = db['product']
    db.close()

    return render_template('retrieveProduct.html', productList=productList, count=len([productList]))


@app.route('/updateProduct/<string:id>/', methods=['GET', 'POST'])
def updateProduct(id):
    updateProductForm = ProductCreate(request.form)
    if request.method == 'POST':
        productList = []
        db = shelve.open('data', 'w')
        productList = db['product']
        for product in productList:
            if product.get_id() == id:
                productList.remove(product)
                product.set_id(updateProductForm.id.data)
                product.set_title(updateProductForm.title.data)
                product.set_cost_price(updateProductForm.costprice.data)
                product.set_retail_price(updateProductForm.retailprice.data)
                product.set_description(updateProductForm.description.data)
                productList.append(product)
        db['product'] = productList
        db.close()
        return redirect(url_for('retrieveProduct'))
    else:
        productList = []
        db = shelve.open('data', 'r')
        productList = db['product']
        db.close()
        for product in productList:
            if product.get_id() == id:
                updateProductForm.id.data = product.get_id()
                updateProductForm.title.data = product.get_title()
                updateProductForm.stock.data = product.get_stock()
                updateProductForm.costprice.data = product.get_cost_price()
                updateProductForm.retailprice.data = product.get_retail_price()
                updateProductForm.description.data = product.display_description()
            else:
                print("asd")
        return render_template('updateProduct.html', form=updateProductForm)


@app.route('/deleteProduct/<string:id>', methods=['POST'])
def deleteproduct(id):
    productList = []
    db = shelve.open('data', 'w')
    productList = db['product']
    for product in productList:
        if product.get_id() == id:
            productList.remove(product)
    db['product'] = productList
    db.close()
    return redirect(url_for('retrieveProduct'))


@app.route('/editpage')
def details():
    return render_template('details.html')


@app.route('/adminPage')
def adminPage():
    return render_template('adminPage.html')


@app.route('/loginPage')
def loginPage():
    return render_template('loginPage.html')


@app.route('/signupPage')
def signupPage():
    return render_template('signupPage.html')


@app.route('/product1')
def product1():
    return render_template('product1.html')


@app.route('/purchasePage')
def purchasePage():
    return render_template('purchasePage.html')


@app.route('/Purchased')
def Purchased():
    return render_template('Purchased.html')


@app.route('/searchPage')
def searchPage():
    return render_template('searchPage.html')


@app.route('/notificationPage')
def notificationPage():
    return render_template('notificationPage.html')


@app.route('/helpPage')
def helpPage():
    return render_template('helpPage.html')


@app.route('/cartPage')
def cartPage():
    return render_template('cartPage.html')


@app.route('/customer_servicePage')
def cutomer_servicePage():
    return render_template('customer_servicePage.html')


@app.route('/FemaleDress1')
def FemaleDress1():
    return render_template('FemaleDress1.html')


@app.route('/pastPurchases')
def pastPurchases():
    return render_template('pastPurchases.html')


@app.route('/productlocationPage')
def productlocationPage():
    return render_template('productlocationPage.html')


if __name__ == '__main__':
    app.run(debug=True)
