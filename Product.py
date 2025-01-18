class Product(object):
    def __init__(self, pid, pname, price, pcat):
        self.product_id = pid
        self.product_name = pname
        self.price = price
        self.category = pcat

    def __str__(self):
        return str(self.product_id) + '\t' + self.product_name + \
                '\t\t' + str(self.price) + '\t' + self.category

    def __repr__(self):
        return str(self.product_id) + '\t' + self.product_name + \
                '\t' + str(self.price) + '\t' + self.category

    def get_product_info(self):
        x = str(self.product_id) + ',' + self.product_name + ',' + str(self.price) + ',' + self.category
        return x.strip('\n')