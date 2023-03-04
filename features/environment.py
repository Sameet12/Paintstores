import time
from features.utility.Utilityclass import UtilityClass


def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    time.sleep(2)

    UtilityClass.maximize_window(context)
    time.sleep(1)

    UtilityClass.launch_app(context)
    time.sleep(2)

def after_scenario(context, driver):
    #context.driver.implicti_wait(3)
    time.sleep(1)
    UtilityClass.close_browser(context)