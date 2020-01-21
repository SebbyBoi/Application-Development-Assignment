from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

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

if __name__=='__main__':
    app.run()