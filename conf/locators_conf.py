#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the home page (home_page.py)
home_page_header = "xpath,//h2[text()='Current temperature']"
current_temperature_text = "xpath,//span[not(contains(@class,'octicon'))]"
buy_button = "xpath,//button[contains(text(), 'Buy %s')]"

#Locators for the product page (product_page.py)
cart_button = "xpath,//button[contains(text(),'Cart')]"
all_product_divs = "xpath,//p[contains(text(),'Price:')]/parent::div"
specific_product_name = "xpath,.//p[contains(@class,'font-weight-bold')]"
product_price = "xpath,.//p[contains(text(),'Price:']"

#Locators for the cart page (cart_page.py)
table_rows = "xpath,//table/descendant::tr"
table_row_by_name = "xpath,//table/descendant::td[text()='%s']"
