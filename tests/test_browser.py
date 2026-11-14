def test_browser_can_open_website(page):
    page.goto("https://www.microsoft.com")

    assert page.title() != ""