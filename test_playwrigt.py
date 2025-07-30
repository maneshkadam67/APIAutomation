
from playwright.sync_api import Page

def test_basic_playwright(playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_page_shortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")



