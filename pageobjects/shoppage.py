from selenium import webdriver
from selenium.webdriver.common.by import By
class shop:
    def __init__(self,driver):
        self.driver=driver
        self.products_path=By.XPATH,"//div[@class='single-products']"
        self.product_path=By.XPATH,"div/p"
        self.add_cart=By.CSS_SELECTOR,"a[class='btn btn-default add-to-cart']"
        self.continue_shopping=By.XPATH,"//button[text()='Continue Shopping']"
        self.cart=By.XPATH,"//li/a/i[@class='fa fa-shopping-cart']"
        self.checkout=By.XPATH,"//a[@class='btn btn-default check_out']"
        self.message=By.XPATH,"//textarea[@name='message']"
        self.place_order=By.XPATH,"//a[@class='btn btn-default check_out']"
    def shopping(self):
        products=self.driver.find_elements(*self.products_path)
        for product in products:
            ITEM=product.find_element(*self.product_path).text
            if ITEM=="Sleeveless Dress":
                product.find_element(*self.add_cart).click()
                break
        self.driver.find_element(*self.continue_shopping).click()
        self.driver.find_element(*self.cart).click()
    def Cart(self):
        self.driver.find_element(*self.checkout).click()
        self.driver.find_element(*self.message).send_keys("Love you Bacche")
        self.driver.find_element(*self.place_order).click() 