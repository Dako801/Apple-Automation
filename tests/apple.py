from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_apple_cart():
    driver = Chrome("//Users/Dakoda/python/_drivers/chromedriver")
    driver.get("https://apple.com")
    driver.find_element_by_xpath('//*[@id="ac-globalnav"]/div/ul[2]/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="chapternav"]/div/ul/li[3]/a/figure').click()
    driver.find_element_by_class_name('ac-ln-button').click()
    driver.find_elements_by_xpath('//*[@class="button button-block"]')[2].click()
    driver.find_element_by_css_selector('button[name="add-to-cart"]').click()
    driver.find_element_by_css_selector('button[class="merchandising button"]').click()
    driver.find_element_by_css_selector('button[id="shoppingCart.actions.checkout"]').click()
    element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "guest-checkout")));
    element.click();
    element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'button[data-autom="continue-button-label"]')));
    element.click();
    element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'input[id="checkout.shipping.addressSelector.newAddress.address.firstName')));
    element.send_keys('Dakoda')
    driver.find_element_by_css_selector('input[id="checkout.shipping.addressSelector.newAddress.address.lastName').send_keys('Nielsen')
    driver.find_element_by_css_selector('input[id="checkout.shipping.addressSelector.newAddress.address.street').send_keys('312 S Main St')
    driver.find_element_by_css_selector('input[id="checkout.shipping.addressSelector.newAddress.address.zipLookup.postalCode').send_keys('84104')
    driver.find_element_by_css_selector('input[id="checkout.shipping.addressContactEmail.address.emailAddress').send_keys('apple@apple.com')
    driver.find_element_by_css_selector('input[id="checkout.shipping.addressContactPhone.address.fullDaytimePhone').send_keys('8011231234')
    driver.find_element_by_css_selector('button[data-autom="continue-button-label"]').click()
    assert driver.title == "Shipping Details — Secure Checkout"
