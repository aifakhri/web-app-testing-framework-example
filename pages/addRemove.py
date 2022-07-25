from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .common import CommonOps

class AddRemoveElement(CommonOps):

    ADD_REMOVE_LINK = (By.LINK_TEXT, "Add/Remove Elements")
    ADD_ELEMENT_BTN = (By.TAG_NAME, "button")
    DELETE_BTN = (By.CLASS_NAME, "added-manually")

    def navigate_to_add_remove_page(self):
        self.wait_for(self.ADD_REMOVE_LINK).click()
    
    def click_add_element_button(self):
        self.wait_for(self.ADD_ELEMENT_BTN).click()

    def check_delete_button(self):
        try: 
            return self.wait_for(self.DELETE_BTN)
        except TimeoutException:
            return "No Delete Button"

    def click_delete_button(self):
        self.find(self.DELETE_BTN).click()

if __name__ == "__main__":
    pass
    
    # url = "https://the-internet.herokuapp.com"
    # driver = webdriver.Firefox()
    # driver.get(url)

    # try:
    #     add_rem = AddRemoveElement(driver)
    #     add_rem.navigate_to_add_remove_page()
    #     add_rem.click_add_element_button()
    #     add_rem.check_delete_button()
    #     print(add_rem.check_delete_button())
    #     add_rem.click_delete_button()
    #     print(add_rem.check_delete_button())
    # finally:
    #     driver.close()