from selenium.webdriver.common.by import By


from .common import CommonOps

from selenium import webdriver

class ContextMenu(CommonOps):

    CONTEXT_MENU = (By.LINK_TEXT, "Context Menu")
    CONTEXT_BOX = (By.ID, "hot-spot")
    PAGE_TITLE = (By.XPATH, "//div[@class='example']/h3")


    def navigate_to_context_menu_page(self):
        self.wait_for(self.CONTEXT_MENU).click()

    def right_click_context_menu(self):
        context_menu = self.find(self.CONTEXT_BOX)
        self.context_click(context_menu).perform()

    def check_alert(self):
        return self.alert()

    def alert_is_accepted(self):
        return self.wait_for(self.PAGE_TITLE).text

if __name__ == "__main__":
    url = "https://the-internet.herokuapp.com"
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        context = ContextMenu(driver)
        context.navigate_to_context_menu_page()
        context.right_click_context_menu()
        
        check_alert = context.check_alert()
        print(check_alert.text)
        check_alert.accept()
    finally:
        driver.close() 