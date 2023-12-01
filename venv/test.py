from conftest import desktop_app
import pytest
from pytest import fixture
from playwright.sync_api import expect
from playwright.sync_api import sync_playwright

'''def test_email(send_email):

        actual_result= str(send_email[1])
        expected_result = "https://news.dbx.so/form/submit?formId=14"
       # locator = page.locator("div.warning")
        assert actual_result == expected_result
def test_youtube(scrolling_site):
    #expected_text = "You are unable to access dbx.so"
    page = scrolling_site[0]
    actual_result = page.locator(selector='text="You are unable to access dbx.so"')
    expect(actual_result).to_have_text("You are unable to access dbx.so")'''
def test_loggin(desktop_app):

    desktop_app.loggin_in()
    expected_result = "https://www.saucedemo.com/inventory.html"
    actual_result_one = list(desktop_app.loggin_in())
    actual_result_two = actual_result_one[0]['url']
    assert actual_result_two == expected_result



