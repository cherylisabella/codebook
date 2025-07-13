""" Superclass Shop and Subclass PopUpShop """
import datetime


class Shop:
    def __init__(self, name: str, address: str, distillery_list: list, employee_list: list, discounts: dict):
        """Initialises one Permanent Shop
        :param name: Name of the shop
        :param address: Address of the shop
        :param distillery_list: All available distilleries at the shop
        :param employee_list: All employees working in this shop
        :param discounts: All discounts which are available in the shop
        """
        self.name = name
        self.address = address
        self.distillery_list = distillery_list
        self.employee_list = employee_list
        self.discounts = discounts

    def __str__(self):
        """Returns a String representation of a shop (only name and address)"""
        return f"Shop name: {self.name}, Address: {self.address}"


class PopUpShop(Shop):
    def __init__(self, name: str, address: str, distillery_list: list, employee_list: list, discounts: dict,
                 start_date: datetime, end_date: datetime):
        """Initialises one pop-up shop
        :param name: Name of the shop
        :param address: Address of the shop
        :param distillery_list: All available distilleries at the shop
        :param employee_list: All employees working in this shop
        :param discounts: All discounts which are available iis shop
        :param start_date: Opening day of the shop
        :param end_date: Closing day of the shop
        """
        super().__init__(name, address, distillery_list, employee_list, discounts)
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        """Returns a String representation of a pop-up shop """
        return f"Shop name: {self.name}, Address: {self.address}, " \
               f"Start date: {self.start_date}, End date: {self.end_date} "
