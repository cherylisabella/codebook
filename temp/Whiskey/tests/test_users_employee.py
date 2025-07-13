""" Test fot the class Employee """
import datetime
import shops
from users import Manager, Employee, shop_list, customer_list
from shops import PopUpShop, Shop

# initialize some variables for testing
manager1 = Manager("Test manager 1", 0)
employee1 = Employee("Test employee", 1)
customer1 = manager1.register_customer("Test customer 2")
manager1.add_shop(PopUpShop("Test Pop up Shop 1", "Test-mania",
                            [1, 2, 3, 4, 5, 6, 9, 18, 19, 20, 21, 22, 23, 24, 30,31, 32, 33, 40, 41, 42, 43, 55],
                            [], {}, datetime.date(2020, 1, 20), datetime.date(2020, 6, 25)))


def test_register_purchase():
    """Test registering 1 purchase for a customer"""
    employee1.register_purchase(1, ["Black Bowmore 42 year old 1964 vintage, 40.5%"], "Shop test1", 0, False)

    assert customer_list[0].transaction_list[0].transaction_id == 1
    assert customer_list[0].customer_name == "Test customer 2"
    assert customer_list[0].transaction_list[0].whiskey == ["Black Bowmore 42 year old 1964 vintage, 40.5%"]


def test_add_change_fav_whiskey():
    """Test adding a favourite distillery and removing it afterward"""
    employee1.add_change_fav_whiskey(1, "Bowmore")
    assert customer_list[0].whiskey_preference == "Bowmore"


def test_remove_fav_whiskey():
    employee1.remove_fav_whiskey(1)
    assert customer_list[0].whiskey_preference == ""


def test_get_next_pop_up_store():
    """test get_next_pop_up_store method return the correct message according to a customer's membership tier"""
    customer_list[0].membership_tier = 'Basic'
    assert employee1.get_next_pop_up_store(1) == "This customer has not the required membership tier" \
                                                 " to get this information"

    customer_list[0].membership_tier = 'Gold'
    assert employee1.get_next_pop_up_store(1) == ["Shop name: Test Pop up Shop 1, Address: Test-mania,"
                                                  " Start date: 2020-01-20"]


def test_get_review():
    result = employee1.get_review("Black Bowmore 42 year old 1964 vintage, 40.5%")
    assert result[0] == "What impresses me most is how this whisky evolves; it's incredibly complex. " \
                        "On the nose and palate, this is a thick, viscous, whisky with notes of sticky toffee, " \
                        "earthy oak, fig cake, roasted nuts, fallen fruit, pancake batter, black cherry, ripe peach, " \
                        "dark chocolate-covered espresso bean, polished leather, tobacco, a hint of wild game, " \
                        "and lingering, leafy damp kiln smoke. Flavors continue on the palate long after swallowing. " \
                        "This is what we all hope for (and dream of) in an older whisky!"


def test_recommend_no_preference():
    manager1.add_shop(shops.Shop('Test 1', 'Test land', [1, 2, 3, 4, 5, 6, 9, 18, 19, 20, 21, 22, 23, 24, 30,
                                                                  31, 32, 33, 40, 41, 42, 43, 55], [], {}))

    result_table = employee1.recommend_no_preference("Bowmore", "Test 1")
    assert result_table.values.tolist() == [97.0, 97.0, 96.0]


# do not work
def test_recommend():
    result_table = employee1.recommend([1, 22, 55], [5, 42], shop_list[0])
    assert list(result_table['RowID']) == [42, 7, 31, 21, 34]

    employee1.add_change_fav_whiskey(1, "Aberlour")
    result = employee1.make_recommendation(1, [22, 55], [5, 42], shop_list[0])
    assert list(result['RowID']) == [42, 7, 31, 21, 34]
