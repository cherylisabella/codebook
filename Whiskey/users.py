""" Class Users and Subclasses Manager and Employee """

import customers
import users  # needed so that whiskey_file and review_file are visible
from shops import Shop, PopUpShop
import datetime
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# stores all customers and shops
customer_list = []
shop_list = []

# stores the files for the recommendation and review system
whiskey_file = pd.read_csv("../whiskey86.csv")
review_file = pd.read_csv("../whiskey_review2020.csv")


class Users:
    def __init__(self, name: str, user_id: int):
        """
        Initialises a user
        :param name: Name of the user
        :param user_id: Unique user id
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """ Returns a String representation of a user """
        return f"User name: {self.name}, user's id: {self.user_id}"


class Manager(Users):
    def __init__(self, name: str, user_id: int):
        """
        Initialises a manager
        :param name: Name of the user
        :param user_id: Unique user id
        """
        super().__init__(name, user_id)

    @staticmethod
    def add_shop(new_shop: Shop):
        """
        Adds a shop to the list of all shops
        :param new_shop: Object of class PopUpShop or Shop
        """
        shop_list.append(new_shop)

    @staticmethod
    def remove_shop(shop_name: str):
        """
        Removes a shop from the list of all shops
        :param shop_name: The name of a shop
        """
        shop = [x for x in shop_list if x.name == shop_name][0]
        shop_list.remove(shop)

    @staticmethod
    def add_discount(shop_name: str, discounts_whiskey: dict):
        """
        Adds one or more discounts to a specific shop
        :param shop_name: Name of a shop
        :param discounts_whiskey: all new discounts
        """
        for i in shop_list:
            if i.name == shop_name:
                # merge existing and new dictionary
                i.discounts = {**i.discounts, **discounts_whiskey}

    @staticmethod
    def remove_discount(shop_name: str, discount_name: str):
        """
        Removes a discount from a specific shop
        :param shop_name: Name of a shop (String)
        :param discount_name: Name of the discount (String)
        """
        [x for x in shop_list if x.name == shop_name][0].discounts.pop(discount_name)

    @staticmethod
    def find_next_customer_id():
        """
        Returns the next available customer id
        :rtype: integer
        """
        if len(customer_list) != 0:
            return customer_list[-1].customer_id + 1
        else:
            return 1

    @staticmethod
    def register_customer(customer_name: str):
        """
        Register a new customer with an automatically generated customer id in the customer list
        :param customer_name: name of new customer
        """
        customer_list.append(customers.Customer(customer_name))

    @staticmethod
    def add_information(path: str):
        """
        Allows the manager to add information to the distillery file ("whiskey_file")
        Column headings of the new two files have to match
        :param path: path to new csv file
        """
        additional_info = pd.read_csv(path)
        users.whiskey_file = pd.concat([users.whiskey_file, additional_info])

    @staticmethod
    def upload_file(path: str, file_type: str):
        """
        Allows the manager to upload different files for the recommendation system, replacing the old ones
        :param path: path to new csv file
        :param file_type: choose "distillery" or "review" to replace chosen file with new file
        """
        replace_file = pd.read_csv(path)
        if file_type == "distillery":
            users.whiskey_file = replace_file
        elif file_type == "review":
            users.review_file = replace_file


class Employee(Users):
    def __init__(self, name: str, user_id: int):
        """
        Initialises an employee
        :param name: Name of the user
        :param user_id: Unique user id
        """
        super().__init__(name, user_id)

    @staticmethod
    def register_purchase(customer_id: int, whiskey: list, shop_name: str, discounts: float, recommendation: bool):
        """
        Registers a purchase as a transaction of a customer
        :param whiskey: whiskeys which are bought
        :param shop_name: name of the shop
        :param discounts: any discounts associated with this purchase?
        :param recommendation: any recommendation associated with this purchase?
        :param customer_id: unique id (int)
        """
        purchase = customers.Transaction(customer_id, whiskey, shop_name, discounts, recommendation)

        for i in customer_list:
            if i.customer_id == customer_id:
                i.transaction_list.append(purchase)
                # update number of purchases and membership tier
                i.total_purchases += 1
                i.no_purchase_within_a_year()
                i.update_tier()

    @staticmethod
    def add_change_fav_whiskey(customer_id: int, favourite_whiskey: str):
        """
        Adds or changes the whiskey/distillery preference of a customer
        :param customer_id: unique customer id
        :param favourite_whiskey: name of favourite_whiskey
        """
        [x for x in customer_list if x.customer_id == customer_id][0].whiskey_preference = favourite_whiskey

    @staticmethod
    def remove_fav_whiskey(customer_id: int):
        """
        Removes the whiskey preference of a customer
        :param customer_id: unique id (int)
        """
        [x for x in customer_list if x.customer_id == customer_id][0].whiskey_preference = ""

    @staticmethod
    def get_next_pop_up_store(customer_id: int):
        """
        Gets the location and time of all upcoming pop-up shops (Gold and Platinum customers only)
        :param customer_id: unique id (int)
        :rtype: String
        """
        # get and check customer´s membership tier
        customer = [x for x in customer_list if x.customer_id == customer_id][0]

        if customer.membership_tier == "Gold" or customer.membership_tier == "Platinum":
            # return all upcoming pop-up shops
            upcoming_shop = [x for x in shop_list if type(x) == PopUpShop and x.start_date <= datetime.date.today()]
            return [f"Shop name: {x.name}, Address: {x.address}, Start date: {x.start_date}" for x in upcoming_shop]
        else:
            return "This customer has not the required membership tier to get this information"

    @staticmethod
    def get_review(whiskey_name: str):
        """
        Gets the reviews about a particular whiskey
        :param whiskey_name: Name of whiskey
        :return: reviews about whiskey
        """
        return users.review_file[users.review_file['name'] == whiskey_name]["description"]

    @staticmethod
    def recommend_no_preference(distillery_name: str, shop_name: str):
        """
        Recommendation system that returns the top 3 reviewed whiskies of a given distillery
        :param shop_name: name of a shop
        :param distillery_name: name of the distillery of interest that is in the shop
        :return: Up to 3 whiskey names with the highest average review score
        """
        # get names in shop distilleries and get all whiskeys from these distilleries
        shop_available_distilleries = [x for x in shop_list if x.name == shop_name][0].distillery_list
        available_search = list(whiskey_file.iloc[shop_available_distilleries, 0:]["Distillery"])
        available_search = review_file[review_file["distillery"].isin(available_search)]

        # get average of every whiskey of a given distillery
        whiskies_table = available_search[available_search["distillery"] == distillery_name].groupby('name')[
                         'points'].mean()
        # return the 3 top reviewed
        return whiskies_table.nlargest(3)

    @staticmethod
    def recommend(distillery_indexes: list, bought_distilleries: list, shop_id: Shop):
        """
        Knn method to return the 5 closest neighbours to the given list of liked distilleries (excluding themselves)
        :param distillery_indexes: indexes of the liked distilleries according to whiskey_file
        :param bought_distilleries: indexes of the bought distilleries according to whiskey_file
        :param shop_id: the shop in shop_list that the customer is in
        :return: the 5 closest distilleries to the given list of liked distilleries (excluding themselves)
        """
        # remove the distilleries that customer already bought from and filter whiskey_file for available distilleries
        shop_available_distilleries = list(set(shop_id.distillery_list) - set(bought_distilleries))
        available_search = whiskey_file.iloc[shop_available_distilleries, 0:]

        # use knn to get the distance from all distilleries to the nearest neighbours
        knn = NearestNeighbors(n_neighbors=8).fit(available_search.iloc[0:, 3:14])
        distances, indices = knn.kneighbors(available_search.iloc[0:, 3:14])

        # save the results from the knn into lists
        closest_index_list, closest_distances_list = [], []

        for i in distillery_indexes:
            relative_index = shop_available_distilleries.index(i)
            closest_index = list(indices[relative_index][1:])
            closest_distances = list(distances[relative_index][1:])
            closest_index_list += closest_index
            closest_distances_list += closest_distances
        result_table = pd.DataFrame({'index': closest_index_list, 'distance': closest_distances_list})

        # remove distilleries input so method don't recommend something the customer know they liked
        for i in range(len(distillery_indexes)):
            result_table = result_table[result_table['index'] != distillery_indexes[i]]

        # get the index of the closest ones and return the distilleries
        result_table = pd.DataFrame(result_table.groupby(["index"])["distance"].min()).nsmallest(columns="distance",
                                                                                                 n=5)
        return available_search.iloc[list(result_table.index), 0:]

    @staticmethod
    def make_recommendation(customer_id, like_distillery_index, bought_distilleries, shop):
        """
        Return the 5 closest neighbours to the given list of liked distilleries of a customer
        :param customer_id: id of customer that want recommendation (this to get their fav distillery in system)
        :param like_distillery_index: indexes of the liked distilleries according to whiskey_file
        :param bought_distilleries: indexes of the bought distilleries according to whiskey_file
        :param shop: the shop in shop_list that the customer is in
        :return: the 5 closest distilleries to the given list of liked distilleries (excluding themselves)
        """
        # extract a customer's favorite distillery from the system and combine it with like_distillery_index
        customer_fav_distillery = customer_list["customer_id" == customer_id].whiskey_preference
        distillery_indexes, customer_fav_distillery_index = [], [0]
        customer_fav_distillery_index[0] = list(users.whiskey_file['Distillery']).index(customer_fav_distillery)
        customer_fav_distillery_index.extend(like_distillery_index)

        # pass the parameters to the users.Employee.recommend method (right above)
        result = users.Employee.recommend(distillery_indexes=customer_fav_distillery_index,
                                          bought_distilleries=bought_distilleries,
                                          shop_id=shop)
        return result


