import time

from behave import *

from datafile import excelutils
from features.pages.PaintStorepageclass import PaintStorePageclass
from features.utility.configclass import ConfigClass




@when("user enters {name} and {email} and {mobile} and {pincode}")
def step_impl(context, name, email, mobile, pincode):

    excelutils.get_row_count(ConfigClass.datafilepath, "Sheet1")

    name = excelutils.read_data(ConfigClass.datafilepath, "Sheet1", 2, 1)
    email = excelutils.read_data(ConfigClass.datafilepath, "Sheet1", 2, 2)
    mobile = excelutils.read_data(ConfigClass.datafilepath, "Sheet1", 2, 3)
    pincode = excelutils.read_data(ConfigClass.datafilepath, "Sheet1", 2, 4)

    ServicesPage = PaintStorePageclass(context.driver)
    ServicesPage.enter_username_textbox(name)
    context.driver.implicitly_wait(1)

    ServicesPage.enter_useremail_textbox(email)
    context.driver.implicitly_wait(1)

    ServicesPage.enter_usermobile_textbox(mobile)
    context.driver.implicitly_wait(1)

    ServicesPage.enter_userpincode_textbox(pincode)
    context.driver.implicitly_wait(1)


@then("it shows valid search result page 2")
def step_impl(context):
    expectedTitle = "Store Locator: Design Solutions for a Beautiful Home Makeover - Asian Paints"
    PageTitle = context.driver.title
    try:
      if (expectedTitle == PageTitle):
          assert True
          print("Test is passed")
          excelutils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 5, "Passed")
      else:
          print("Test is failed")
          excelutils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 5, "Failed")
          assert False
      time.sleep(1)
    finally:
        print("page title is" + PageTitle)
        time.sleep(1)
