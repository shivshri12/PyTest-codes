import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import Helper
import allure
from allure_commons.types import AttachmentType

file = r"C:\Users\shivendra.shrivastav\Downloads\Test_Data1.xlsx"

@pytest.fixture
@allure.severity(allure.severity_level.NORMAL)
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # open browser in maximized mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
@allure.severity(allure.severity_level.CRITICAL)
def test_account_creation(setup):
    driver = setup
    driver.get("http://10.206.6.62:92/Pages/Login.aspx")

    # Login
    driver.find_element(By.ID,'txtLoginName').send_keys('portalsuperuser')
    driver.find_element(By.ID,'txtLoginPwd').send_keys('Test123!')
    driver.find_element(By.ID,'btnLogin').click()
    time.sleep(5)

    # Home check
    assert driver.find_element(By.XPATH,'//*[@id="ctl00_CPMain_lblhome"]').is_displayed()
    print("✅ Home is present")

    # Navigation
    driver.find_element(By.XPATH,'/html/body/form/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/section/ul/li[5]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/form/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/section/div/section/div[5]/div/ul/li[8]/a').click()
    time.sleep(5)

    # Excel rows loop
    rows = Helper.noofrows(file, "Sheet1")

    for r in range(2, rows+1):
        firstname = Helper.readdata(file, 'Sheet1', r, 1)
        lastname  = Helper.readdata(file, 'Sheet1', r, 2)
        gender    = Helper.readdata(file, 'Sheet1', r, 3)
        address   = Helper.readdata(file, 'Sheet1', r, 4)
        city      = Helper.readdata(file, 'Sheet1', r, 5)
        state     = Helper.readdata(file, 'Sheet1', r, 6)
        postal    = Helper.readdata(file, 'Sheet1', r, 7)
        email     = Helper.readdata(file, 'Sheet1', r, 8)
        phone     = Helper.readdata(file, 'Sheet1', r, 9)
        dob       = Helper.readdata(file, 'Sheet1', r, 10)
        idtype    = Helper.readdata(file, 'Sheet1', r, 11)
        idname    = Helper.readdata(file, 'Sheet1', r, 12)
        idnumber  = Helper.readdata(file, 'Sheet1', r, 13)
        acf3      = Helper.readdata(file, 'Sheet1', r, 14)
        acf4      = Helper.readdata(file, 'Sheet1', r, 15)
        acf5      = Helper.readdata(file, 'Sheet1', r, 16)
        acf8      = Helper.readdata(file, 'Sheet1', r, 17)

        # Fill the form
        driver.find_element(By.ID,'ctl00_CPMain_ddlClientname').send_keys('ANZ Client')
        driver.find_element(By.ID,'ctl00_CPMain_ddlProduct').send_keys('ANZ_TravelCard')
        driver.find_element(By.ID,'ctl00_CPMain_txtSACActivationCode').send_keys('1212')
        driver.find_element(By.ID,'ctl00_CPMain_ddlPlasticCode').send_keys('ANZ Travel Design A')

        driver.find_element(By.ID,'ctl00_CPMain_txtFirstname').send_keys(firstname)
        driver.find_element(By.ID,'ctl00_CPMain_txtLastname').send_keys(lastname)
        driver.find_element(By.ID,'ctl00_CPMain_ddlGender').send_keys(gender)
        driver.find_element(By.ID,'ctl00_CPMain_txtAddress').send_keys(address)
        driver.find_element(By.ID,'ctl00_CPMain_txtCity').send_keys(city)
        driver.find_element(By.ID,'txtZipcode1').send_keys(postal)
        driver.find_element(By.ID,'ctl00_CPMain_ddlState').send_keys(state)
        driver.find_element(By.ID,'ctl00_CPMain_txtEmail').send_keys(email)
        driver.find_element(By.ID,'txtDob').send_keys(dob)
        driver.find_element(By.ID,'ctl00_CPMain_txtMobNo2').send_keys(phone)
        driver.find_element(By.ID,'FieldTitleUf3').send_keys(acf3)
        driver.find_element(By.ID,'FieldTitleUf4').send_keys(acf4)
        driver.find_element(By.ID,'FieldTitleUf5').send_keys(acf5)
        driver.find_element(By.ID,'FieldTitleUf8').send_keys(acf8)
        time.sleep(3)
        driver.find_element(By.ID,'addRow_1').click()
        time.sleep(3)
        Select(driver.find_element(By.ID,'ddlIDType')).select_by_visible_text(idtype)
        Select(driver.find_element(By.ID,'ddlIDName')).select_by_visible_text(idname)
        driver.find_element(By.ID,'txtIDNumber').send_keys(idnumber)
        driver.find_element(By.ID,'btnSubmitPopUpID').click()
        time.sleep(3)

        driver.find_element(By.NAME,'ctl00$CPMain$chkVerify').click()
        driver.find_element(By.ID,'ctl00_CPMain_ddlWallet').send_keys('Australian Dollar')
        time.sleep(3)
        driver.find_element(By.ID,'ctl00_CPMain_txtLoadAmount').send_keys('500.00')
        driver.find_element(By.ID,'ctl00_CPMain_btnAdd').click()
        time.sleep(5)
        driver.find_element(By.ID,'btnSubmit').click()
        time.sleep(7)

        result = driver.find_element(By.ID,'ctl00_CPMain_idAcctext1').is_displayed()

        if result:
            Helper.writedata(file,'Sheet1',r,18,'Passed')
            Helper.fillGreencolor(file,'Sheet1',r,18)
        else:
            Helper.writedata(file,'Sheet1',r,18,'Failed')
            Helper.fillRedcolor(file,'Sheet1',r,18)

        assert result == True   # pytest ko pass/fail batane ke liye
        allure.attach(driver.get_screenshot_as_png(),name='screenshot',attachment_type=AttachmentType.PNG)

        driver.find_element(By.ID,'btnNewCard').click()




