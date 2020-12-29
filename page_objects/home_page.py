"""
Models the home page of weather shopper
"""
from .Base_Page import Base_Page
import conf.locators_conf as LOCATORS

class Home_Page(Base_Page):
    "Home page of the application"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/'
        self.open(url)

    def get_temperature(self):
        "Get the temperature"
        temperature_text = self.get_text(LOCATORS.current_temperature_text)
        self.write(temperature_text)
