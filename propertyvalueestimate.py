from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import domainapi as api


addressId = 2017019671
def getPropertySoup(addressId, headless=False):

    url = "https://www.domain.com.au/" + addressId
    chromeOptions = Options()

        # Should open window or not?
    if headless:
        chromeOptions.add_argument("--headless")

    WINDOW_SIZE = "1920,1080"
    chromeOptions.add_argument("--window-size=%s" % WINDOW_SIZE)
    chromeOptions.add_argument("disable-notifications")

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)
    driver.save_screenshot("screenshot.png")

    # Try getting xpath element if not specified scroll and wait as necessary
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')))
    except:
        pass
    finally:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

    return soup

def getPropertyValue(propertySoup):
    propertyValue = propertySoup.find_all("div", class_= "text-input__value-renderer has-icon-left is-outside css-ko6f1y")
    propertyValue = [_.text for _ in propertyValue]
    propertyValue = propertyValue[0].replace(",", "").replace("%", "")
    print("The property value is", propertyValue)

    return int(propertyValue)

if __name__ == '__main__':

    # Page name is the string in the ur of page after www.facebook.com/
    soup = getPropertySoup("2017019671")
    print(getPropertyValue(soup))
