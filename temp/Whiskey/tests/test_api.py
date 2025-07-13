""" Test for the API """
import api
from flask import Flask

import users


def test_welcome():
    app = api.app
    client = app.test_client()

    url = '/'
    response = client.get(url)
    assert response.get_data() == b'{"Title": "This is a whiskey sales system"}'
    assert response.status_code == 200


def test_create_customer():
    app = api.app
    client = app.test_client()

    url = '/manager/register_customer:MAX'
    response = client.get(url)
    assert response.get_data() == b'{"message": "The customer MAX has been registered with the customer id 1!"}'
    assert response.status_code == 200


def test_post_permanent_shop():
    app = api.app
    client = app.test_client()

    url = '/manager/add_permanent_shop:shop1:Maastricht:1,5,10,20:name_emp:{}'
    response = client.get(url)
    assert response.get_data() == b'{"message": "The permanent shop shop1 has been added!"}'
    assert response.status_code == 200

    url = '/manager/add_permanent_shop:shop1:Maastricht:hi,5,10,20:name_emp:{}'
    response = client.get(url)
    assert response.get_data() == b'{"error": "The shop shop1 could not be created!"}'
    assert response.status_code == 400


def test_post_popup_shop():
    app = api.app
    client = app.test_client()

    url = "/manager/add_popup_shop:shop2:Maastricht:1,5,10,20:name_emp:{}:2022-01-01:2022-06-01"
    response = client.get(url)
    assert response.get_data() == b'{"message": "The pop-up shop shop2 has been added!"}'
    assert response.status_code == 200

    url = "/manager/add_popup_shop:shop2:Maastricht:1,test,10,20:name:{}:2022-01-01:2022-06-01"
    response = client.get(url)
    assert response.get_data() == b'{"error": "The shop shop2 could not be created!"}'
    assert response.status_code == 400


def test_remove_shop():
    app = api.app
    client = app.test_client()
    url = '/manager/remove_shop:shop2'

    response = client.get(url)
    assert response.get_data() == b'{"message": "The shop shop2 has been removed!"}'
    assert response.status_code == 200

    url = '/manager/remove_shop:shop3'
    response = client.get(url)
    assert response.get_data() == b'{"error": "The shop shop3 does not exist!"}'
    assert response.status_code == 400


def test_post_discount():
    app = api.app
    client = app.test_client()

    url = "/manager/add_discount:shop1&{'discount1': 0.4}"
    response = client.get(url)
    assert response.get_data() == b'{"message": "The discounts have been added to the shop shop1!"}'
    assert response.status_code == 200

    url = "/manager/add_discount:shop5&{}"
    response = client.get(url)
    assert response.get_data() == b'{"error": "The shop shop5 does not exist!"}'
    assert response.status_code == 400

    url = "/manager/add_discount:shop1&discounts"
    response = client.get(url)
    assert response.get_data() == b'{"error": "The discounts is not in the form of a dictionary!"}'
    assert response.status_code == 400


def test_delete_discount():
    app = api.app
    client = app.test_client()

    url = "/manager/remove_discount:shop1:discount1"
    response = client.get(url)
    assert response.get_data() == b'{"message": "The discount discount1 from shop shop1 has been removed!"}'
    assert response.status_code == 200

    url = "/manager/remove_discount:shop3:discount1"
    response = client.get(url)
    assert response.get_data() == b'{"error": "The shop shop3 or discount discount1 does not exist!"}'
    assert response.status_code == 400


# Test employee functions
def test_post_purchase():
    app = api.app
    client = app.test_client()

    # create a testing customer
    # client.get('/manager/register_customer:MAX')

    url = '/employee/register_purchase:1:Test_whiskey:shop1:0:False'
    response = client.get(url)
    assert response.get_data() == b'{"message": "The purchase has been registered!"}'
    assert response.status_code == 200

    # test for non registered customer
    url = '/employee/register_purchase:50:Test_whiskey:shop1:0:False'
    response = client.get(url)
    assert response.get_data() == b'{"error": "The customer id does not exist!"}'
    assert response.status_code == 400

    # test for incorrect transaction input (correct customer_id)
    url = '/employee/register_purchase:1:Test_whiskey:shop1:Bug:False'
    response = client.get(url)
    assert response.get_data() == b'{"error": "Cannot add the information to the file!"}'
    assert response.status_code == 400


def test_post_fav_whiskey():
    app = api.app
    client = app.test_client()

    url = '/employee/register_fav_whiskey:1:Bowmore'
    response = client.get(url)
    assert response.get_data() == b'{"message":"The whiskey preference has been registered!"}'
    assert response.status_code == 200

    url = '/employee/register_fav_whiskey:50:Bowmore'
    response = client.get(url)
    assert response.get_data() == b'{"error":"The customer id does not exist!"}'
    assert response.status_code == 400


def test_delete_fav_whiskey():
    app = api.app
    client = app.test_client()

    url = '/employee/remove_fav_whiskey:1'
    response = client.get(url)
    assert response.get_data() == b'{"message": "The whiskey preference has been removed!"}'
    assert response.status_code == 200

    url = '/employee/remove_fav_whiskey:50'
    response = client.get(url)
    assert response.get_data() == b'{"error":"The customer id does not exist!"}'
    assert response.status_code == 400


def test_get_popup_store():
    app = api.app
    client = app.test_client()

    #create a testing customer and testing popup shop
    client.get('/manager/register_customer:MAX')
    client.get("/manager/add_popup_shop:shop_name2:Maastricht:1,5,10,20:name_emp:{}:2022-01-01:2022-06-01")

    url = '/employee/get_popup_store:1'
    response = client.get(url)
    assert response.get_data() == b'{"message": "{"name":"shop_name2",' \
                                  b'"address":"Maastricht",' \
                                  b'"distillery_list":"{1,5,10,20}",' \
                                  b'"employee_list":"name_emp",' \
                                  b'"discounts":{},' \
                                  b'"start_date":"2022-01-01",' \
                                  b'"end_date":"2022-06-01""}}\n'
    assert response.status_code == 200

    url = '/employee/get_popup_store:50'
    response = client.get(url)
    assert response.get_data() == b'{"error": "The customer id does not exist!"}\n'
    assert response.status_code == 400


def test_get_review():
    app = api.app
    client = app.test_client()

    url = '/employee/get_review:"Black+Bowmore+42+year+old+1964+vintage,+40.5%"'
    response = client.get(url)
    assert response.get_data() == b'{"message": "What impresses me most is how this whisky evolves; it\'s ' \
                                  b'incredibly complex. On the nose and palate, this is a thick, viscous, whisky ' \
                                  b'with notes of sticky toffee, earthy oak, fig cake, roasted nuts, fallen fruit, ' \
                                  b'pancake batter, black cherry, ripe peach, dark chocolate-covered espresso bean, ' \
                                  b'polished leather, tobacco, a hint of wild game, and lingering, leafy damp ' \
                                  b'kiln smoke. Flavors continue on the palate long after swallowing. This is what we ' \
                                  b'all hope for (and dream of) in an older whisky!"}\n'
    assert response.status_code == 200


def test_get_recommendation():
    app = api.app
    client = app.test_client()

    # create test shop
    client.get("/manager/add_permanent_shop:shop1:Maastricht:1,5,10,20:name_emp:{}")

    url = '/employee/recommendation_no_preference:"Bowmore"'
    response = client.get(url)
    real_result = users.Employee.recommend_no_preference(distillery_name="Bowmore", shop_name="shop1")
    assert response.get_data() == {'message': real_result}
    assert response.status_code == 200


def test_get_recommendation_2():
    app = api.app
    client = app.test_client()

    # create test shop
    client.get("/manager/add_permanent_shop:shop1:Maastricht:1,5,10,20,25,30:name_emp:{}")
    client.get("/manager/register_customer:MAX")
    real_result = users.Employee.make_recommendation(customer_id=1, like_distillery_index=[5],
                                                     bought_distilleries=[10], shop=users.shop_list[0])

    url = '/employee/recommendation_preference:1:[5]:[10]:users.shop_list[0]'
    response = client.get(url)
    assert response.get_data() == {'message': real_result}
    assert response.status_code == 200


def test_post_file():
    app = api.app
    client = app.test_client()

    url = '/manager/upload_file:../tests/whiskey_86_test.csv:distillery'
    response = client.get(url)
    assert response.get_data() == b'{"message": "The file has been uploaded!"}'
    assert response.status_code == 200

    url = '/manager/upload_file:../tests/whiskey_86_test.csv:test'
    response = client.get(url)
    assert response.get_data() == b'{"error": "This file type does not exist!"}'
    assert response.status_code == 400

    url = '/manager/upload_file:../tests/test/whiskey_86_test.csv:test'
    response = client.get(url)
    assert response.get_data() == b'{"error": "Can not find the file!"}'
    assert response.status_code == 400


def test_post_information():
    app = api.app
    client = app.test_client()

    url = '/manager/upload_file:../tests/whiskey_86_test.csv'
    response = client.get(url)
    assert response.get_data() == b'{"message": "The information has been added to the file!"}'
    assert response.status_code == 200

    url = '/manager/upload_file:../tests/test/whiskey_86_test.csv'
    response = client.get(url)
    assert response.get_data() == b'{"error": "Cannot add the information to the file!"}'
    assert response.status_code == 400
