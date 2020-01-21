class Product:
    def __init__(self, id, title, description, stock, cost_price, retail_price, image):
        self.__id = id
        self.__title = title
        self.description = description
        self.__stock = stock
        self.__cost_price = cost_price
        self.__retail_price = retail_price
        self.__image = image

    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    #def get_description(self):
    #    return self.__description
    def get_stock(self):
        return self.__stock
    def get_cost_price(self):
        return self.__cost_price
    def get_retail_price(self):
        return self.__retail_price
    def get_image(self):
        return self.__image

    def set_id(self, id):
        self.__id = id
    def set_title(self, title):
        self.__title = title
    def set_description(self, description):
        self.description = description
    def set_stock(self, stock):
        self.__stock = stock
    def set_cost_price(self, cost_price):
        self.__cost_price = cost_price
    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price
    def set_image(self, image):
        self.__image = image

    def display_description(self):
        return "%s" % (self.description)