import time
from playwright.sync_api import  Playwright
class App:
    def __init__(self,playwright : Playwright):
        self.browser=playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://www.saucedemo.com/")

    def loggin_in(self):
        #self.page.get_by_label("User Name").fill("standard_user")
        self.page.locator(selector="//*[@id='user-name']").fill("standard_user")
        time.sleep(2)
        self.page.locator('//*[@id="password"]').fill("secret_sauce")
        time.sleep(2)
        self.page.wait_for_selector(selector='//*[@id="login-button"]').click()
        time.sleep(2)
        resulted_page = self.page.url

        yield {'url': resulted_page}
        #yield resulted_page

    def go_to_basket(self):
        self.page.locator(selector='//*[@id="shopping_cart_container"]/a[1]').click()
        self.page.locator(selector='//*[@id="checkout"]').click
        self.page.get_by_label("First Name").fill("Dmytro")
        self.page.get_by_label("Last Name").fill("Buvalets")
        self.page.get_by_label("Zip/Postal Code").fill("228228")
        self.page.locator(selector='//*[@id="continue"]').click()
        self.page.locator(has_text='')
        resulted_page = self.page.url
        yield resulted_page_basket

    def go_to_linkedin(self):
        self.page.locator(selector='//*[@id="page_wrapper"]/footer[1]/ul[1]/li[3]/a[1]').click()
        resulted_page = self.page.url
        yield resulted_page
    def close_machine(self):
        self.page.close()
        self.context.close()
        self.browser.close()









    '''def go_to_tokenization(self):
        self.page.goto ("https://dbx.so")
        self.page.wait_for_selector(selector='text="Buy DBX"').click()
        self.page.wait_for_selector(selector='text="Bitforex"').click()
    def close_machine(self):
        self.page.close()
        self.context.close()
        self.browser.close()'''