"""
Models the home page of weather shopper
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as LOCATORS

class Home_Page(Base_Page):
    "Home page of the application"
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/'
        self.open(url)

    @Wrapit._screenshot
    def get_temperature(self):
        "Get the temperature"
        temperature_text = 25
        temperature_text = self.get_text(LOCATORS.current_temperature_text)
        temperature_text = temperature_text.split()[0]
        temperature_text = int(temperature_text)
        result_flag = False
        if type(temperature_text) == int:
            result_flag = True
        self.conditional_write(result_flag,
        positive=f'Obtained the temperatrure {temperature_text}',
        negative='Could not obtain the temperature',
        level='debug')

        return temperature_text

    @Wrapit._screenshot
    def click_buy_button(self, product_type):
        "Click the right buy button"
        result_flag = self.click_element(LOCATORS.buy_button%product_type)
        self.conditional_write(result_flag,
        positive=f'Found the {product_type} buy button',
        negative=f'Could not find the {product_type} buy button',
        level='debug')

        result_flag &= self.check_element_present(LOCATORS.cart_button)
        self.conditional_write(result_flag,
        positive=f'Clicked the {product_type} button',
        negative=f'Could not click the {product_type} button',
        lelve='debug')

        return result_flag

    def decide(self):
        "Decide what to purchase"
        result_flag = False
        temperature = self.get_temperature()
        if temperature <= 19:
            result_flag = self.click_buy_button('moisturizers')
        if temperature >= 34:
            result_flag = self.click_buy_button('sunscreens')

        return result_flag