from selenium import webdriver
from selenium.webdriver.common.by import By
class payment:
    def __init__(self,driver):
        self.driver=driver
        self.cardname=By.NAME,"name_on_card"
        self.cardnum=By.NAME,"card_number"
        self.cvc=By.NAME,"cvc"
        self.expiry_month=By.NAME,"expiry_month"
        self.expiry_year=By.XPATH,"//input[@class='form-control card-expiry-year']"
        self.submit=By.ID,"submit"
        self.confirmation=By.XPATH,"//p[@style='font-size: 20px; font-family: garamond;']"
        self.continue_button=By.XPATH,"//a[@class='btn btn-primary']"
    def payment_details(self):
        self.driver.find_element(*self.cardname).send_keys("stokes")
        self.driver.find_element(*self.cardnum).send_keys("987456321")
        self.driver.find_element(*self.cvc).send_keys("852")
        self.driver.find_element(*self.expiry_month).send_keys("1")
        self.driver.find_element(*self.expiry_year).send_keys("2025")
        self.driver.find_element(*self.submit).click()
    def greet(self):
        greet=self.driver.find_element(*self.confirmation).text
        print(greet)
        self.driver.find_element(*self.continue_button).click()
        