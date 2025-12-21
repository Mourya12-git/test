from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.accountpage import Account
from pageobjects.shoppage import shop
from pageobjects.paymentpage import payment
import json
path="F:\Bunty\PythonPractice\SeleniumScripts\project2\data.json"
with open(path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]
    
import pytest

@pytest.mark.parametrize("test_list_item",test_list)
def test_execution(browserinstance,test_list_item):
    driver=browserinstance
    acc=Account(driver)
    acc.accountcreation(test_list_item["username"],test_list_item["email"])
    if acc.count<1:
        
        acc.acc_details(test_list_item["password"],test_list_item["firstname"],test_list_item["lastname"])
    shop_obj=shop(driver)
    shop_obj.shopping()
    shop_obj.Cart()
    pay_obj=payment(driver)
    pay_obj.payment_details()
    pay_obj.greet()
    
