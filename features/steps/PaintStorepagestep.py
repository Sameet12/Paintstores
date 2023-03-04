import time
from hamcrest import *
from behave import *
from selenium.webdriver.common.by import By

from features.pages.PaintStorepageclass import PaintStorePageclass

@given(u'Chrome is opened and asian paints app is opened')
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Trusted Wall Painting, Home Painting & Waterproofing in India - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when("Customer clicks on not now button")
def step_impl(context):
    time.sleep(6)
    Allowvalue = PaintStorePageclass(context.driver)
    Allowvalue.click_Allow_Button()


@when(u'Customer is able to click on PaintStores link')
def step_impl(context):
    time.sleep(3)
    mousehover = PaintStorePageclass(context.driver)
    mousehover.mousehover()
    time.sleep(2)
    paintstores = PaintStorePageclass(context.driver)
    paintstores.clicklinks()

@step("Customer enters pincode '122001'")
def step_impl(context):
    time.sleep(10)
    pincode = PaintStorePageclass(context.driver)
    pincode.enter_pincode_text()
    time.sleep(10)

@step("Customer clicks on cookie close button")
def step_impl(context):
    time.sleep(10)
    cookiecrossbutton = PaintStorePageclass(context.driver)
    cookiecrossbutton.click_cookie_button()


'''@step("Customer is able to scroll the window")
def step_impl(context):
    time.sleep(10)
    context.execute_script("window.scrollBy(0,600);")'''


@when(u'Customer is able to access store locator button')
def step_impl(context):
    time.sleep(10)
    storelocatorbutton = PaintStorePageclass(context.driver)
    storelocatorbutton.click_storelocator_Button()



@then(u'It shows PaintStores page')
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Store Locator: Design Solutions for a Beautiful Home Makeover - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when(u'Customer is able to click on view details button')
def step_impl(context):
    viewbutton = PaintStorePageclass(context.driver)
    viewbutton.click_viewdetails_Button()


@then(u'It shows the page AP Beautiful Homes Furniture & Paint Store for House Decoration')
def step_impl(context):
    time.sleep(5)
    expectedTitle = "AP Beautiful Homes Furniture & Paint Store for House Decoration - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

#@step("Customer enters pincode 831004")
#def step_impl(context):
   # time.sleep(10)
    #pincode = PaintStorePageclass(context.driver)
    #pincode.enter_pincode_text()

@then(u'It shows the stores')
def step_impl(context):
    expectedTitle = "Store Locator: Design Solutions for a Beautiful Home Makeover - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'customer enters {uname} and {uemail} and {umobile} and {upincode}')
def step_impl(context, uname, uemail, umobile, upincode):
    PaintStorePage = PaintStorePageclass(context.driver)

    PaintStorePage.enter_username_textbox(uname)
    time.sleep(1)

    PaintStorePage.enter_useremail_textbox(uemail)
    time.sleep(1)

    PaintStorePage.enter_usermobile_textbox(umobile)
    time.sleep(1)

    PaintStorePage.enter_userpincode_textbox(upincode)
    time.sleep(1)


@when(u'Customer is able to click on Enquire Now Button')
def step_impl(context):
    time.sleep(5)
    context.driver.implicitly_wait(2)
    Paintstorepage = PaintStorePageclass(context.driver)
    Paintstorepage.click_EnquireNow_Button()

@then(u'it shows Thankyou image')
def step_impl(context):
    time.sleep(6)
    PaintStorePage = PaintStorePageclass(context.driver)
    expectedText = " Thank you!"
    actualText = context.driver.find_element(By.CLASS_NAME, PaintStorePage.Thankyou).text
    print(actualText)
    assert_that(expectedText, actualText, "Text is not same")


@step("Customer is not able to click on Enquire Now Button")
def step_impl(context):
    time.sleep(10)
    enquirenowbutton = PaintStorePageclass(context.driver)
    enquirenowbutton.click_EnquireNow_Button()


@then("It is on the same page")
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Store Locator: Design Solutions for a Beautiful Home Makeover - Asian Paints"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))




