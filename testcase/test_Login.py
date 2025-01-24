import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from testcase.log import Loggenerator
from utilities.xlutils import ReadData, Count, Writedata


class Test_Automation:
    XLPATH = "C:\\Users\\pradi\\OneDrive\\Desktop\\Daily  Update.xlsx"

    def test_Functionaltest(self, Setup):
        self.driver = Setup
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed()
            assert True
        except:
            assert False

    # @pytest.mark.skip
    def test_parameterization(self, Setup, getdataforlogin):
        self.driver = Setup
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(getdataforlogin[0])
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(getdataforlogin[1])
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # self.wait=WebDriverWait(self.driver,10)
        # Dashboard=self.driver.find_element(By.XPATH,"//h6[text()='Dashboard']")
        # self.wait.until(expected_conditions.visibility_of_element_located(Dashboard))

        try:
            self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed()
            assert True
        except:
            assert False

    # @pytest.mark.skip
    def test_DDT_validation(self, Setup):
        self.driver = Setup
        self.driver.implicitly_wait(5)
        self.maxRow = Count(self.XLPATH, 'Sheet1')
        # self.login_status = self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        self.log = Loggenerator.logger()
        self.log.info("ENter in DDT")

        for i in range(1, self.maxRow + 1):
            self.xl = ReadData(self.XLPATH, 'Sheet1', 1, i)
            self.password = ReadData(self.XLPATH, 'Sheet1', 2, i)
            self.Expected_result = ReadData(self.XLPATH, "Sheet1", 3, i)
            self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(self.xl)
            self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(self.password)
            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            if self.driver.title == 'OrangeHRM':
                if self.Expected_result == 'pass':
                    Writedata(self.XLPATH, 'Sheet1', 4, i, 'pass')
                elif self.Expected_result == 'fail':
                    Writedata(self.XLPATH, 'Sheet1', 4, i, 'fail')

    def test_Dynamic(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys('Credencetest@test.com')
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//h3[text()='Apple Macbook Pro']").click()
        # Click Login button
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # Click on Continue Shopping
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        # Click on Product--Headphone
        self.driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()
        # Click on add to cart
        self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # Click on Continue Shopping
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        # Click on Product--Ipad
        self.driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()
        # Click on add to cart
        self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)
        # Select Quality dropdown value for product 1
        product_quantity1 = Select(self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select"))
        product_quantity1.select_by_index(3)
        # Select Quality dropdown value for product 2
        product_quantity2 = Select(self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select"))
        product_quantity2.select_by_index(3)
        # Select Quality dropdown value for product 3
        product_quantity3 = Select(self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select"))
        product_quantity3.select_by_index(2)

        l = len(self.driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
        # l=6

        Product_Price_List = []
        for r in range(1, l - 2):
            var1 = self.driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            product_price = (var1[1:])
            Product_Price_List.append(float(product_price))

        Exp_Subtotal = round((sum(Product_Price_List)), 2)
        # Exp_Subtotal-->11999.889999999998
        # Exp_Subtotal-->11999.89
        print("Exp_Subtotal-->" + str(Exp_Subtotal))

        print(Product_Price_List)

        System_Value = []

        for r in range(l - 2, l + 1):
            var2 = self.driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            system_price = (var2[1:])
            System_Value.append(system_price)
            time.sleep(5)

        print(System_Value)
