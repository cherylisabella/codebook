""" Test the methods """

import shops
import users

# initialize some variables for testing
shop_id = shops.Shop(name='Test 1', address='Test land', distillery_list=[1, 2, 3, 4, 5, 6, 9, 18, 19, 20, 21, 22, 23,
                                                                          24, 30, 31, 32, 33, 40, 41, 42, 43, 55],
                     employee_list=[], discounts={})
test_employee = users.Employee(name="Test employee", user_id=0)


def test_recommend_no_preference():
    result_table = test_employee.recommend_no_preference("Bowmore", shop_id=shop_id)
    assert result_table.values.tolist() == [97.0, 97.0, 96.0]


def test_recommend():
    result_table = test_employee.recommend([1, 22, 55], [5, 42], shop_id)
    assert list(result_table['RowID']) == [42, 7, 31, 21, 34]
