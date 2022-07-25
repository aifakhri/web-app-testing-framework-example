from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


from .common import CommonOps

from selenium import webdriver
from time import sleep

class DynamcControls(CommonOps):

    DYNAMIC_CONTROL = (By.LINK_TEXT, "Dynamic Controls")
    CHECKBOX_LOCATOR = (By.XPATH, "//input[@type='checkbox']")
    CHECKBOX_BTN = (By.XPATH, "//form[@id='checkbox-example']/button")
    INPUT_TEXT_LOCATOR = (By.XPATH, "//input[@type='text']")
    INPUT_TEXT_BTN = (By.XPATH, "//form[@id='input-example']/button")
    ELEMENT_INFO = (By.ID, "message")
    

    def navigate_to_dynamic_controls_page(self):
        self.wait_for(self.DYNAMIC_CONTROL).click()

    def check_checkbox_element(self):
        try:
            self.wait_for(self.CHECKBOX_LOCATOR)
            return ("Checkbox Element Presents")
        except TimeoutException:
            return ("No Checkbox Element")

    def remove_checkbox(self):
        self.find(self.CHECKBOX_BTN).click()
        self.wait_for(self.ELEMENT_INFO)

    def add_checkbox(self):
        self.find(self.CHECKBOX_BTN).click()
        self.wait_for(self.ELEMENT_INFO)

    def checking_input_text_element(self):
        return self.wait_for(self.INPUT_TEXT_LOCATOR).is_enabled()

    def enable_disable_input_text(self):
        self.find(self.INPUT_TEXT_BTN).click()
        self.wait_for(self.ELEMENT_INFO)


if __name__ == "__main__":
    url = "https://the-internet.herokuapp.com"
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        control = DynamcControls(driver)
        control.navigate_to_dynamic_controls_page()
    #     control.check_checkbox_element()
    #     control.remove_checkbox()

        
    #     print(control.check_checkbox_element())
    #     control.add_checkbox()
    #     control.check_checkbox_element()
        print(control.checking_input_text_element())
        control.enable_disable_input_text()
        print(control.checking_input_text_element())
        # insert_text = control.writing_string_to_input_text("this is testing")
        # print(insert_text.get_attribute('value'))
    finally:
        driver.close() 