""" API for the Whiskey Sales System """
from flask import Flask
import datetime
import customers
import users
import json
import ast
from shops import PopUpShop, Shop

app = Flask(__name__)

# create one manager and employee
manager = users.Manager("Max Mustermann", 1)
employee = users.Employee("John Doe", 2)


@app.route('/')
def welcome():
    return json.dumps({'Title': "This is a whiskey sales system"}), 200


# manager
@app.get('/manager/register_customer:<name>')
def create_customer(name):
    manager.register_customer(name)
    assigned_id = users.customer_list[-1].customer_id
    return json.dumps({'message': f"The customer {name} has been registered with the customer id {assigned_id}!"}), 200


@app.get('/manager/add_permanent_shop:<name>:<address>:<distillery_list>:<employee_list>:<discounts>')
def post_permanent_shop(name, address, distillery_list, employee_list, discounts):
    # create permanent shop
    try:
        distillery_list = distillery_list.split(',')
        distillery_list = [int(x) for x in distillery_list]
        employee_list = employee_list.split(',')
        discounts = ast.literal_eval(discounts)
        shop = Shop(name, address, distillery_list, employee_list, discounts)
    except:
        return json.dumps({'error': f"The shop {name} could not be created!"}), 400
    # add shop

    manager.add_shop(shop)
    return json.dumps({'message': f"The permanent shop {name} has been added!"}), 200


@app.get('/manager/add_popup_shop:<name>:<address>:<distillery_list>:<employee_list>:<discounts>:<start_date>:'
         '<end_date>')
def post_popup_shop(name, address, distillery_list, employee_list, discounts, start_date, end_date):
    # create pop-up shop
    try:
        distillery_list = distillery_list.split(',')
        distillery_list = [int(x) for x in distillery_list]
        employee_list = employee_list.split(',')
        discounts = ast.literal_eval(discounts)
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        shop = PopUpShop(name, address, distillery_list, employee_list, discounts, start_date, end_date)
    except:
        return json.dumps({'error': f"The shop {name} could not be created!"}), 400
    # add shop
    manager.add_shop(shop)
    return json.dumps({'message': f"The pop-up shop {name} has been added!"}), 200


@app.get('/manager/remove_shop:<name>')
def remove_shop(name):
    try:
        manager.remove_shop(name)
        return json.dumps({'message': f"The shop {name} has been removed!"}), 200
    except:
        return json.dumps({'error': f"The shop {name} does not exist!"}), 400


@app.get('/manager/add_discount:<shop_name>&<discount_dictionary>')
def post_discount(shop_name, discount_dictionary):
    # convert discounts from string to dictionary
    try:
        discount_dictionary = ast.literal_eval(discount_dictionary)
    except:
        return json.dumps({'error': "The discounts is not in the form of a dictionary!"}), 400

    # check if shop exists
    exists = False
    for i in users.shop_list:
        if i.name == shop_name:
            exists = True

    if exists:
        manager.add_discount(shop_name, discount_dictionary)
        return json.dumps({'message': f"The discounts have been added to the shop {shop_name}!"}), 200
    else:
        return json.dumps({'error': f"The shop {shop_name} does not exist!"}), 400


@app.get('/manager/remove_discount:<shop_name>:<discount_name>')
def delete_discount(shop_name, discount_name):
    try:
        manager.remove_discount(shop_name, discount_name)
        return json.dumps({'message': f"The discount {discount_name} from shop {shop_name} has been removed!"}), 200
    except:
        return json.dumps({'error': f"The shop {shop_name} or discount {discount_name} does not exist!"}), 400


@app.get('/manager/upload_file<path>:<file_type>')
def post_file(path, file_type):
    # check type
    if file_type != "distillery" or file_type != "review":
        return json.dumps({'error': "This file type does not exist!"}), 400
    # replace file
    try:
        manager.upload_file(path, file_type)
        return json.dumps({'message': "The file has been uploaded!"}), 200
    except FileNotFoundError:
        return json.dumps({'error': "Can not find the file!"}), 400


@app.get('/manager/add_information:<path>')
def post_information(path):
    try:
        manager.add_information(path)
        return {'message': "The information has been added to the file!"}, 200
    except:
        return {'error': "Cannot add the information to the file!"}, 400


# Employee
@app.get('/employee/register_purchase:<customer_id>:<whiskey>:<shop_name>:<discount>:<recommendation>')
def post_purchase(customer_id, whiskey, shop_name, discount, recommendation):
    # check customer id
    check_id = [x for x in users.customer_list if x.customer_id == customer_id]
    if len(check_id) == 0:
        return json.dumps({'error': "The customer id does not exist!"}), 400

    # create transaction
    try:
        whiskey = whiskey.split()
        discount = float(discount)
        if recommendation == "true":
            recommendation = True
        purchase = customers.Transaction(whiskey, shop_name, discount, recommendation)
    except:
        return json.dumps({'error': "The transaction could not be created - invalid input!"}), 400

    # register purchase
    employee.register_purchase(customer_id, purchase)
    return {'message': "The purchase has been registered!"}, 200


@app.get('/employee/register_fav_whiskey:<customer_id>:<fav_whiskey>')
def post_fav_whiskey(customer_id, fav_whiskey):
    # check customer id
    check_id = [x for x in users.customer_list if x.customer_id == customer_id]
    if len(check_id) == 0:
        return json.dumps({'error': "The customer id does not exist!"}), 400

    # register favourite whiskey
    employee.add_change_fav_whiskey(customer_id, fav_whiskey)
    return json.dumps({'message': "The whiskey preference has been registered!"}), 200


@app.get('/employee/remove_fav_whiskey:<customer_id>')
def delete_fav_whiskey(customer_id):
    # check customer id
    check_id = [x for x in users.customer_list if x.customer_id == customer_id]
    if len(check_id) == 0:
        return json.dumps({'error': "The customer id does not exist!"}), 400

    # register favourite whiskey
    employee.remove_fav_whiskey(customer_id)
    return not json.dumps({'message': "The whiskey preference has been removed!"}), 200


@app.get('/employee/get_popup_store:<customer_id>')
def get_popup_store(customer_id):
    # check customer id
    check_id = [x for x in users.customer_list if x.customer_id == customer_id]
    if len(check_id) == 0:
        return {'error': "The customer id does not exist!"}, 400

    # register favourite whiskey
    result = employee.get_next_pop_up_store(customer_id)
    return {'message': result}, 200


@app.get('/employee/get_review:<whiskey_name>')
def get_review(whiskey_name):
    result = employee.get_review(whiskey_name)
    return {'message': result}, 200


@app.get('/employee/recommendation_no_preference:<distillery_name>')
def get_recommendation(distillery_name):
    result = employee.recommend_no_preference(distillery_name)
    return {'message': result}, 200


@app.get('/employee/recommendation_preference:<customer_id><like_distillery_index><bought_distilleries><shop>')
def get_recommendation_2(customer_id, like_distillery_index, bought_distilleries, shop):
    like_distillery_index = like_distillery_index.split()
    bought_distilleries = bought_distilleries.split()
    # register favourite whiskey
    result = employee.make_recommendation(customer_id, like_distillery_index, bought_distilleries, shop)
    return {'message': result}, 200


if __name__ == '__main__':
    app.run(debug=True)
