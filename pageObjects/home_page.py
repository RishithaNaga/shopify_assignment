import time

from pycparser.ply.yacc import resultlimit
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import new_window_is_opened


class Home_page:
    link_becomepartner_xpath="//a[contains(text(),'Become a partner')]"
    button_beforelogin_xpath="//a[contains(text(),'Log in')]"
    input_email_xpath="//input[@class='next-input email-typo-input']"
    link_continuewithemail_xpath="//span[contains(text(),'Continue with email')]"
    input_password_xpath="//input[@label='Password']"
    button_afterlogin_xpath="//span[contains(text(),'Log in')]"
    button_usernameelement_xpath="(//div[@class='Polaris-InlineStack'])[2]"
    button_logintostore_xpath="//span[@class='Polaris-Button__Text' and contains(text(),'Log in')]"
    chooseanaccount_accountlink="//div[@class='user-card__email' and contains(text(),'nagarishitha181292@gmail.com')]"
    button_Apps_xpath="//span[contains(text(),'Apps')]"
    #button_Apps_xpath="//*[@class='Polaris-Navigation__Text']/descendant::span[text()='Products']"
    pumperbundle_searchresult_xpath="//*[@class='Polaris-InlineStack' and text()='Pumper Bundles Quantity Breaks']"
    create_offer_button_xpath = "//*[text()='Create offer' or text()='Create new offer']/parent::button"
    create_a_quantity_break_xpath = "//*[text()='Create a Quantity Break']/parent::button"
    select_a_product_xpath="//*[text()='Select a Product']/parent::button"
    product_selection_checkbox_xpath = "//*[@aria-label='Select: women skirts']/child::*[contains(@class, 'Checkbox')]/descendant::input"
    add_button_xpath = "//*[text()='Add']/parent::button"
    limited_time_period_template_xpath="//*[text()='Limited Time Offer']/ancestor::*[@class='template_bundle_container active']"
    apply_selected_template_button="//span[text()='Apply selected template']/parent::button"
    publish_button="//*[text()='Publish']/parent::button"
    products_navigation_xpath= "//*[@class='Polaris-Navigation__Text']/child::*[text()='Products']"
    product_preview_online_locator = "//*[text()='women skirts']/parent::a/following-sibling::*[contains(@class, '_PreviewLink')]/descendant::a"
    add_to_cart_button="//span[contains(text(),'Add to cart')]/parent::button"
    cart_logo_button="//a[@class='header__icon header__icon--cart link focus-inset']"
    product_quantity_input="//input[@class='quantity__input']"
    product_price_text="//*[@class='cart-item__totals right small-hide']/descendant::*[@class='price price--end']"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def navigate_to_google(self):
        self.driver.get("https://www.shopify.com/partners/")
        self.driver.maximize_window()

    def goto_shopifypartners(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,Home_page.link_becomepartner_xpath)).click().perform()
        actions.move_to_element(self.driver.find_element(By.XPATH,Home_page.button_beforelogin_xpath)).click().perform()
        email_element=self.driver.find_element(By.XPATH,Home_page.input_email_xpath)
        email_element.clear()
        email_element.send_keys("nagarishitha181292@gmail.com")
        time.sleep(5)
        self.driver.find_element(By.XPATH,Home_page.link_continuewithemail_xpath).click()
        password_element=self.driver.find_element(By.XPATH,Home_page.input_password_xpath)
        password_element.clear()
        password_element.send_keys("Shopify@123")
        time.sleep(5)
        self.driver.find_element(By.XPATH,Home_page.button_afterlogin_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,Home_page.button_usernameelement_xpath).click()
        current_window=self.driver.current_window_handle
        self.driver.find_element(By.XPATH,Home_page.button_logintostore_xpath).click()
        all_window_handles=self.driver.window_handles
        all_window_handles.remove(current_window)
        new_window_handle = all_window_handles[0]
        self.driver.switch_to.window(new_window_handle)
        self.driver.find_element(By.XPATH,Home_page.chooseanaccount_accountlink).click()
        actions = ActionChains(self.driver)
        #actions.move_to_element(self.driver.find_element(By.XPATH,Home_page.button_Apps_xpath)).click().perform()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,Home_page.button_Apps_xpath))

        #self.driver.find_element(By.XPATH,Home_page.button_Apps_xpath).click().
        self.driver.find_element(By.XPATH, Home_page.pumperbundle_searchresult_xpath).click()
        time.sleep(5)

        self.driver.switch_to.frame("app-iframe")
        actions = ActionChains(self.driver)
        actions.scroll_to_element(self.driver.find_element(By.XPATH, Home_page.create_offer_button_xpath)).perform()
        self.driver.find_element(By.XPATH, Home_page.create_offer_button_xpath).click()

        actions.move_to_element(self.driver.find_element(By.XPATH, Home_page.create_a_quantity_break_xpath)).click().perform()
        actions.move_to_element(self.driver.find_element(By.XPATH, Home_page.select_a_product_xpath)).click().perform()
        self.driver.switch_to.default_content()
        actions = ActionChains(self.driver)
        actions.click(self.driver.find_element(By.XPATH, Home_page.product_selection_checkbox_xpath)).perform()
        self.driver.find_element(By.XPATH, Home_page.add_button_xpath).click()
        self.driver.switch_to.frame("app-iframe")
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, Home_page.limited_time_period_template_xpath)).click().perform()
        self.driver.find_element(By.XPATH,Home_page.apply_selected_template_button).click()
        self.driver.find_element(By.XPATH,Home_page.publish_button).click()

        self.driver.switch_to.default_content()
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, Home_page.products_navigation_xpath)).click().perform()
        actions.move_to_element(self.driver.find_element(By.XPATH, Home_page.product_preview_online_locator)).perform()
        self.driver.find_element(By.XPATH, Home_page.product_preview_online_locator).click()
        time.sleep(5)
        third_window_handle = self.driver.window_handles[2]
        self.driver.switch_to.window(third_window_handle)
        result = self.driver.find_element(By.XPATH,"//*[contains(text(), 'Limited Time Offer')]").is_displayed()
        assert result

        actions.move_to_element(self.driver.find_element(By.XPATH,Home_page.add_to_cart_button)).click().perform()
        actions.move_to_element(self.driver.find_element(By.XPATH,Home_page.cart_logo_button)).click()
        quantity=self.driver.find_element(By.XPATH,Home_page.product_quantity_input).get_attribute("value")
        assert quantity==2

        price=self.driver.find_element(By.XPATH,Home_page.product_price_text).text
        assert price.strip(" ")=="Rs. 36.00"
        print("END", result)






