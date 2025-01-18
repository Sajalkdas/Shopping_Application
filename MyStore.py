from Product import Product


class MyStore(object):
    def __init__(self):
        self.plist = []

    def read_products_from_file(self, fname):
        self.plist = []
        with open(fname, mode='r') as file:
            for line in file:
                parts = line.split(',')
                pr = Product(int(parts[0]), parts[1], parts[2], parts[3])
                self.plist.append(pr)
        return self.plist

    def show_products(self):
        print('\n')
        for pr in self.plist:
            print(pr, end='')

    def get_product(self, pid):
        for pr in self.plist:
            if pr.product_id == pid:
                return pr
        return None

    def remove_product(self, file_name, p):
        with open(file_name, mode='w') as file:
            for index, product in enumerate(p):
                if index == len(p) - 1:
                    file.write(product.get_product_info().strip('\n'))
                else:
                    file.write(product.get_product_info() + '\n')


def add_product(file_name, prod):
   with open(file_name, mode='a') as file:
       file.write('\n' + prod.get_product_info())


