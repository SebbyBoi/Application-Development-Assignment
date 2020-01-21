import shelve
#with shelve.open("data", "r") as db:
#    productList = db['product']
#    for product in productList:
#        print(product.get_id())

db = shelve.open('data', 'w')
productList = db['product']
for product in productList:
    print(type(product.get_id()))
db.close()

