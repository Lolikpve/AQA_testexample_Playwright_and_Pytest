import time
import re
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, devtools=False)
    page = browser.new_page()
    page.goto("https://dbx.so")
    page.wait_for_selector(selector='text="Contact us"').click()
    page.fill(selector="//*[@id='mauticform_input_dbxcontactus_user_name']", value="Lolitas")
    page.fill(selector="//*[@id='mauticform_input_dbxcontactus_user_email']", value="Lolitas@gmail.com")
    page.click(selector="//*[@id='mauticform_input_dbxcontactus_submit']")
    # page.locator(selector='text="Contact us"').click()
    page.text_content()
    time.sleep(2)
    # time.sleep(3)
    browser.close()


