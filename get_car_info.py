def get_car_info(s):
    # Get the car make from the user
    INFO = input("Enter the {}:".format(s))
    # Small user input validation for now
    if not INFO:
        print("Check the {} on https://cargurus.com".format(s))
        print("Please enter a valid {}".format(s))
        get_car_info(s)
    else:
        return INFO


def get_zip_code():
    ZIP_CODE = input("Enter your Zip Code:")
    # Small user input validation for now
    if not ZIP_CODE.isdigit() or len(ZIP_CODE) != 5:
        print("Please enter a valid zip code")
        get_zip_code()
    else:
        return ZIP_CODE


def get_info():

    CAR_MAKE = get_car_info("Make")
    CAR_MODEL = get_car_info("Model")
    ZIP_CODE = get_zip_code()
    print("MAKE: {}, MODEL: {}, ZIP CODE: {}".format(
        CAR_MAKE, CAR_MODEL, ZIP_CODE))
    return (CAR_MAKE, CAR_MODEL, ZIP_CODE)
