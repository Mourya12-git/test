from selenium import webdriver
from selenium.webdriver.common.by import By
class Account:
    def __init__(self,driver):
        self.driver=driver
        self.login_signup=By.XPATH,"//a[text()=' Signup / Login']"
        self.name=By.NAME,"name"
        self.email=By.XPATH,"//input[@data-qa='signup-email']"
        self.signup=By.XPATH,"//button[@data-qa='signup-button']"
        self.count=0
        self.gender=By.ID,"id_gender1"
        self.password=By.ID,"password"
        self.day=By.ID,"days"
        self.month=By.ID,"months"
        self.year=By.ID,"years"
        self.newsletter=By.ID,"newsletter"
        self.offers=By.ID,"optin"
        self.firstname=By.ID,"first_name"
        self.lastname=By.ID,"last_name"
        self.address=By.ID,"address1"
        self.country_id=By.ID,"country"
        self.state=By.ID,"state"
        self.city=By.ID,"city"
        self.pincode=By.ID,"zipcode"
        self.mobile_no=By.ID,"mobile_number"
        self.create_account=By.XPATH,"//button[@data-qa='create-account']"
        self.Continue=By.XPATH,"//a[@data-qa='continue-button']"
    def accountcreation(self,Name,email):
        self.driver.find_element(*self.login_signup).click()
        self.driver.find_element(*self.name).send_keys(Name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.signup).click()
        mess=self.driver.find_element(By.XPATH,"//p[@style='color: red;']").text
        self.count=0
        if mess in "Email Address already exist!":
            self.driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys(email)
            self.driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys("Mourya@12")
            self.driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()
            self.count+=1
        
    def acc_details(self,password,firstname,lastname):
        self.driver.find_element(*self.gender).click()
        self.driver.find_element(*self.password).send_keys(password)
        from selenium.webdriver.support.ui import Select
        Day=Select(self.driver.find_element(*self.day))
        Day.select_by_value("12")
        Month=Select(self.driver.find_element(*self.month))
        Month.select_by_visible_text("September")
        Year=Select(self.driver.find_element(*self.year))
        Year.select_by_value("2004")
        self.driver.find_element(*self.newsletter).click()
        self.driver.find_element(*self.offers).click()
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.address).send_keys("SRPT")
        dropdown=Select(self.driver.find_element(*self.country_id))
        dropdown.select_by_visible_text("India")
        self.driver.find_element(*self.state).send_keys("Telangana")
        self.driver.find_element(*self.city).send_keys("Suryapet")
        self.driver.find_element(*self.pincode).send_keys("508213")
        self.driver.find_element(*self.mobile_no).send_keys("1234567895")
        self.driver.find_element(*self.create_account).click()
        self.driver.find_element(*self.Continue).click()
        