import pickle
from os import path
class ShoppingItem(object):
    def __init__(self, prod, qty):
        self.product = prod
        self.quantity = qty


class ShoppingCart(object):
    def __init__(self):
        self.items = []
        self.plist = []
        self.load_pickle()

    def add_item(self, product, qty):
        sitem = ShoppingItem(product, qty)
        self.items.append(sitem)

    def remove_item(self, pid):
        for item in self.items:
            if item.product.product_id == pid:
                self.items.remove(item)
                break

    def compute_total(self):
        total = 0
        for item in self.items:
            total = total + item.product.price * item.quantity
        return total

    def apply_discount(self, total):
        if total > 100 and total < 500:
            total = total - (total * 5/100)
        elif total > 500 and total < 1000:
            total = total - (total * 10/100)
        else:
            total = total - (total * 15/100)
        return total

    def show_cart(self):
        for item in self.items:
            print('\t\t' + item.product.__str__().replace('\n', '') +
                  '\tqty=' + str(item.quantity))

    def clear_cart(self):
        self.items = []
        print("\tCart is cleared!")

    def save_pickle(self, pickle_file, plist_pickle_file):
        with open(pickle_file, mode='wb') as cart_pickle_file:
            pickle.dump(self.items, cart_pickle_file)
        with open(plist_pickle_file, mode='wb') as plist_file:
            pickle.dump(self.plist, plist_file)

    def load_pickle(self):
        if path.exists('cart_pickle_file.bin'):
            with open("cart_pickle_file.bin", mode='rb') as cart_pickle_file:
                deserialized_items = pickle.load(cart_pickle_file)
            self.items = deserialized_items
