from product import Product
import shelve

product_list = []
Product1 = Product('1', "Black Female Clothes", "Description for this clothes", 100, 20, 30, "/static/img/Black Female Clothes Long Sleeve 1.png")
Product2 = Product('2', "Female Long Sleeve Jacket", "Description for this clothes", 100, 21, 31, "/static/img/Female Long Sleeve Jacket 1.png")
Product3 = Product('3', "Female Long Sleeve Clothes", "Description for this clothes", 100, 22, 32, "/static/img/Female Long Sleeve Clothes 1.png")
Product4 = Product('4', "Female One Piece Dress", "Description for this clothes", 100, 23, 33, "/static/img/Female one piece dress 1.png")

product_list.append(Product1)
product_list.append(Product2)
product_list.append(Product3)
product_list.append(Product4)

with shelve.open("data", "c") as db:
    db["product"]=product_list

