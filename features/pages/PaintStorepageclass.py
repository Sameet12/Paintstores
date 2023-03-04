import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class PaintStorePageclass:


    def __init__(self, driver):

        self.Thankyou = "thankYouTitle"
        self.driver = driver

        # Element locators values
        self.hover = "(//span[@class='iconTextLinks__text visible-in-Desktop'])[3]"
        self.PaintsLink = "(//li[@class='dropdown__item--list-item'])[27]"
        self.viewdetailsButtonElement = "(//*[normalize-space(text())='VIEW DETAILS'])[1]"
        self.pincodetextElement = "//input[@id='search-input']"
        self.storelocatorButtonElement ="//*[@id='aroundme-btn']"
        self.cookieclose = "//div[@id='onetrust-close-btn-container']/button"
        #self.storelocatorButtonElement = "/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]/form/div/span"
        self.usernameTextBoxElement ="//input[@id='enquire-name']"
        self.useremailTextBoxElement ="//input[@id='enquire-email']"
        self.usermobileTextBoxElement = "//input[@id='enquire-mobile']"
        self.userpincodeTextBoxElement ="//input[@id='enquire-pincode']"
        self.FrameElement = "//*[@id='__st_fancy_popup']/iframe"
        self.NotNowElement = "//input[@value='Not Now']"
        self.EnquireNowButtonElement ="(//button[@class='ctaText enquireForm--step-1-submit track_form_submit'])[1]"
    def mousehover(self):
        hovering = self.driver.find_element(By.XPATH, self.hover)
        action = ActionChains(self.driver)
        action.move_to_element(hovering)
        action.perform()
    def clicklinks(self):
        Link = self.driver.find_element(By.XPATH, self.PaintsLink)
        Link.click()

    def click_viewdetails_Button(self):
        viewdetails_Button = self.driver.find_element(By.XPATH, self.viewdetailsButtonElement)
        viewdetails_Button.click()

    def enter_pincode_text(self):
        pin = self.driver.find_element(By.XPATH, self.pincodetextElement)
        pin.send_keys(831004)

    def click_storelocator_Button(self):
        storelocatorButton = self.driver.find_element(By.XPATH, self.storelocatorButtonElement)
        storelocatorButton.click()

    def enter_username_textbox(self, uname):
        usernameTextBox = self.driver.find_element(By.XPATH, self.usernameTextBoxElement)
        usernameTextBox.send_keys(uname)

    def enter_useremail_textbox(self, uemail):
        useremailTextBox = self.driver.find_element(By.XPATH, self.useremailTextBoxElement)
        useremailTextBox.send_keys(uemail)

    def enter_usermobile_textbox(self, umobile):
        usermobileTextBox = self.driver.find_element(By.XPATH, self.usermobileTextBoxElement)
        usermobileTextBox.send_keys(umobile)

    def enter_userpincode_textbox(self, upincode):
        userpincodeTextBox = self.driver.find_element(By.XPATH, self.userpincodeTextBoxElement)
        userpincodeTextBox.send_keys(upincode)

    def click_EnquireNow_Button(self):
        EnquireNowButton = self.driver.find_element(By.XPATH, self.EnquireNowButtonElement)
        EnquireNowButton.click()

    def click_cookie_button(self):
        closebutton = self.driver.find_element(By.XPATH, self.cookieclose)
        closebutton.click()

    def click_Allow_Button(self):
        Frame = self.driver.find_element(By.XPATH, self.FrameElement)
        self.driver.switch_to.frame(Frame)
        clickAllowButton = self.driver.find_element(By.XPATH, self.NotNowElement)
        clickAllowButton.click()
        time.sleep(50)
        self.driver.switch_to.default_content()


