from pytest import fixture
import time
import re
import pytest
from playwright.sync_api import sync_playwright , expect
from page_objects.application import App

###Fixture for initializating Playwright and yielding to our POM class###
@pytest.fixture(scope="session")
def get_playwright():
    with sync_playwright() as playwright:
        #yield playwright.chromium.launch(headless=False)
        yield playwright

###Fixture for Page Object Model###
@pytest.fixture(scope="session")
def desktop_app(get_playwright):
    app = App(get_playwright)
    yield app
    app.close_machine()










'''@pytest.fixture(scope="session")
def send_email(browser):
    with browser as b:

        page = b.new_page()
        page.goto("https://dbx.so")
        page.wait_for_selector(selector='text="Contact us"').click()
        page.fill(selector="//*[@id='mauticform_input_dbxcontactus_user_name']", value="Lolitas")
        page.fill(selector="//*[@id='mauticform_input_dbxcontactus_user_email']", value="Lolitas@gmail.com")
        page.click(selector="//*[@id='mauticform_input_dbxcontactus_submit']")
        #text_locator = page.locator(".")
        #expect().

        time.sleep(2)
        # time.sleep(3)
        resulted_page = page.url
        #browser.close()
        yield [page , resulted_page]

@pytest.fixture(scope="session")
def scrolling_site(send_email):
    page = send_email[0]
    page.goto("https://dbx.so")
    page.wait_for_selector(selector='//*[@id="page"]/main[1]/section[2]/div[1]/div[1]/div[3]/a[1]/div[1]/h2[1]').click()
    #page.wait_for_selector(selector="//*[@id='page']/footer[1]/div[1]/div[1]/div[3]/ul[1]/li[3]/a[1]/svg[1]").click()
    resulted_page= page.url
    yield [page , resulted_page]
    time.sleep(2)'''



