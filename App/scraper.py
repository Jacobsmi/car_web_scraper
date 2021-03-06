import config
import database_controller as db
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
class Scraper:
    def __init__(self):
        self.CARS = []

    def parse_info(self,titles, prices, miles):
        for x in range(len(titles)-1):
            '''
            title_parts[0] = Year
            title_parts[1] = Make
            title_parts[2] = Model
            
            Other parts represent options and can be handled together
            '''
            mile = int(miles[x].text.replace(",","").replace(" mi",""))
            price = int(prices[x].text.replace("$", "").replace(",",""))
            title_parts = titles[x].text.split(" ")
            options = ""
            for y in range(3,len(title_parts)):
                if y != len(title_parts):
                    options += title_parts[y] + " "
                else:
                    options += title_parts[y]
            self.CARS.append([title_parts[0], title_parts[1], title_parts[2], options, price, mile])

    def get_car_page(self,CAR_MAKE, CAR_MODEL, ZIP_CODE):
        # Create an instance of the driver with the argument pointing to chromedriver on system
        driver = webdriver.Chrome(config.PATH_TO_WEB_DRIVER)
        # Navigate the webpage to selected URL
        driver.get("https://www.cargurus.com/")

        # Driver finds element on the page with HTML id carPickerUsed_makerSelect
        # Then it is turned into an instance of the Select class imported from selenium
        maker_select = Select(driver.find_element_by_id('carPickerUsed_makerSelect'))
        try:
            # select_by_visible_text is then called on the Select object that has just been created which selects
            # the option in that dropdown with the specified text
            maker_select.select_by_visible_text(CAR_MAKE)
        except:
            driver.close()
            return "make_error"

        # The above steps are then repeated for the make and year
        model_select = Select(driver.find_element_by_id('carPickerUsed_modelSelect'))
        try:
            model_select.select_by_visible_text(CAR_MODEL)
        except: 
            driver.close()
            return "model_error"
        try:
            # Finds the Zip Code field by ID with the find element by ID method
            zip_code_entry = driver.find_element_by_id("dealFinderZipUsedId_dealFinderForm")
            # Uses Keys send_keys function to type Zip Code then press "Enter" key
            zip_code_entry.send_keys(ZIP_CODE)
            zip_code_entry.send_keys(Keys.RETURN)
        except: 
            driver.close()
            return "zip_code_error"
        # This try except loop attempts to get all the raw information for the cars by
        # pulling text, found by class, right off the page 
        sleep(2)
        
        try:
            print("Trying to get information")
            titles = driver.find_elements_by_class_name("_4BPaqe")
            prices = driver.find_elements_by_class_name("_4SFkcZ")
            miles = driver.find_elements_by_class_name("qUF2aQ")
        
        except:
            driver.close()
            return "title_parsing_error"
        
        try:
            return(self.parse_info(titles, prices, miles))        
        except: 
            return "parsing_error"
            
        input("Press enter when done")
        return None