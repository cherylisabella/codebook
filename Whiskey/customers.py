""" Classes Customer and Transaction """
import datetime
import users


class Customer:
    def __init__(self, customer_name: str):
        """Initialises a new customer
        :param customer_name: Customer´s full name
        """
        self.customer_name = customer_name
        self.customer_id = users.Manager.find_next_customer_id()
        self.whiskey_preference = ""
        self.membership_tier = "None"
        self.transaction_list = []
        self.total_purchases = 0
        self.purchases_one_year = 0

    def no_purchase_within_a_year(self):
        """Determine number of transactions during the last year"""
        now = datetime.datetime.today()
        one_year_ago = now.replace(year=now.year-1)
        # traverse through transaction list
        count = len([x for x in self.transaction_list if x.date >= one_year_ago])
        self.purchases_one_year = count

    def update_tier(self):
        """ Updates the membership tier"""
        if self.purchases_one_year >= 50:
            self.membership_tier = "Platinum"
        elif self.purchases_one_year >= 25:
            self.membership_tier = "Gold"
        elif self.purchases_one_year >= 10:
            self.membership_tier = "Silver"
        else:  # becomes default after first purchase
            self.membership_tier = "Basic"

    def find_next_transaction_id(self):
        """Returns the next available transaction id (purchases)
        :rtype: integer
        """
        if len(self.transaction_list) > 0:
            return self.transaction_list[-1].transaction_id + 1
        else:
            return 1

    def __str__(self):
        """ Returns a String representation of a customer with the most important information """
        return f"Customer name: {self.customer_name}, Id: {self.customer_id}, " \
               f"Membership tier: {self.membership_tier}, Whiskey preference: {self.whiskey_preference}"


class Transaction:
    def __init__(self, customer_id: int, whiskey: list, shop_name: str, discounts: float, recommendation: bool):
        """
        Creates one transaction between a customer and shop (purchase)
        :param customer_id: Unique customer id
        :param whiskey: whiskeys which are bought
        :param shop_name: name of the shop
        :param discounts: any discounts associated with this purchase?
        :param recommendation: any recommendation associated with this purchase?
        """
        customer = [x for x in users.customer_list if x.customer_id == customer_id][0]

        self.transaction_id = customer.find_next_transaction_id()
        self.whiskey = whiskey
        self.date = datetime.datetime.now()
        self.shop = shop_name
        self.discounts = discounts
        self.recommendation = recommendation

    def __str__(self):
        """ Returns a String representation of a customer with the most important information """
        return f"Transaction id: {self.transaction_id}, Whiskeys: {self.whiskey} "
