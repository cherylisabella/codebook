""" Test for Classes Customer and Transaction """
import customers
import users

# initialise a manager and employee
manager = users.Manager("Test manager", 1)
employee = users.Employee("Test employee", 2)

# register customer
manager.register_customer("Test customer")
test_customer = users.customer_list[0]


def test_transaction():
    # register purchases
    for i in range(30):
        employee.register_purchase(test_customer.customer_id, ["Chivas Regal Ultis 40%"], "Shop 1", 0, False)
    # check correct number of purchases and correct transaction id
    assert len(users.customer_list[0].transaction_list) == 30
    assert users.customer_list[0].transaction_list[29].transaction_id == 30


def test_number_of_purchases():
    # variables are updated automatically when purchases are registered
    assert test_customer.total_purchases == 30
    assert test_customer.purchases_one_year == 30


def test_update_tier():
    # variable is updated automatically when purchases are registered
    assert test_customer.membership_tier == "Gold"


def test_find_next_transaction_id():
    result = test_customer.find_next_transaction_id()
    assert result == 31
