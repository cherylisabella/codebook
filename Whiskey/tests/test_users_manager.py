""" Tests for Class Manager """

import datetime
from users import Manager, shop_list, customer_list, users
from shops import PopUpShop, Shop

# initialize some variables for testing
manager1 = Manager("John", 1)
manager1.add_shop(PopUpShop("Test Shop 1", "Test-mania", [1, 2, 3, 4, 5, 6, 55], [], {},
                            datetime.date(2020, 1, 25), datetime.date(2020, 6, 25)))


def test_find_next_customer_id():
    """test to see if find_next_customer_id is automatically update when a new customer is added"""
    assert manager1.find_next_customer_id() == 1
    manager1.register_customer("Test customer")
    assert manager1.find_next_customer_id() == 2


def test_add_shop():
    """testing for add_popup_shop, add_shop and remove_shop methods"""
    manager1.add_shop(PopUpShop("Test Shop 2", "Test-mania", [1, 2, 3, 4, 5, 6, 55], [], {},
                                datetime.date(2020, 1, 25), datetime.date(2020, 6, 25)))
    manager1.add_shop(Shop("Test Shop 3", "Den Haag", [1, 2, 3], [], {}))

    assert len(shop_list) == 3
    assert shop_list[1].name == 'Test Shop 2'
    assert shop_list[1].distillery_list == [1, 2, 3, 4, 5, 6, 55]
    assert shop_list[1].start_date == datetime.date(2020, 1, 25)
    assert shop_list[2].name == "Test Shop 3"
    assert shop_list[2].distillery_list == [1, 2, 3]


def test_remove_shop():
    manager1.remove_shop("Test Shop 3")
    assert len(shop_list) == 2


def test_add_discount():
    manager1.add_discount("Test Shop 1", {"Black Bowmore 42 year old 1964 vintage, 40.5%": 0.25})
    assert users.shop_list[0].discounts == {"Black Bowmore 42 year old 1964 vintage, 40.5%": 0.25}


def test_remove_discount():
    manager1.remove_discount("Test Shop 1", "Black Bowmore 42 year old 1964 vintage, 40.5%")
    assert users.shop_list[0].discounts == {}


def test_register_customer():
    manager1.register_customer("Test customer 1")
    assert customer_list[1].customer_name == 'Test customer 1'
    assert customer_list[1].customer_id == 2

    manager1.register_customer("Test customer 2")
    assert customer_list[2].customer_name == 'Test customer 2'
    assert customer_list[2].customer_id == 3


def test_add_information():
    """ test adding the same whiskey86.csv to existing one see if the len doubled"""
    path = "../whiskey86.csv"
    manager1.add_information(path)
    assert len(users.whiskey_file) == 172


def test_upload_files():
    # whiskey86_test.csv is a 5 lines version of whiskey86.csv
    replace_whiskey_path = "../tests/whiskey86_test.csv"
    manager1.upload_file(replace_whiskey_path, "distillery")
    assert len(users.whiskey_file) == 5

    # whiskey_review2020_test.csv is a 5 lines version of whiskey_review2020.csv
    replace_review_path = "../tests/whiskey_review2020_test.csv"
    manager1.upload_file(replace_review_path, "review")
    assert len(users.review_file) == 5
