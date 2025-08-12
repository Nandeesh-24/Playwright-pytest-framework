import re
from playwright.sync_api import expect


def test_google_page(page):
    page.goto('https://google.com')

    try:
        page.get_by_role('button', name='Accept all').click(timeout=3000)
    except:
        print("No popup found")

    page.get_by_role('combobox', name='Search').fill('playwright')
    page.keyboard.press('Enter')

    expect(page).to_have_title(re.compile('playwright', re.IGNORECASE))