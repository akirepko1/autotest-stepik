link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    button = len(browser.find_elements_by_class_name("btn-primary"))
    assert button > 0, '!!!НЕ НАШЕЛ!!!'
