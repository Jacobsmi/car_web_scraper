import config
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def get_car_page(CAR_MAKE, CAR_MODEL, ZIP_CODE):
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
    input("Press enter when done")
    return None
