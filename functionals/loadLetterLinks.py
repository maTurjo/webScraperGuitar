from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .saveLinkForLetterList import saveLinkForLetterList


def loadLetterLinks(driver: WebDriver):
    website = "https://tabs.ultimate-guitar.com/tab/shuvro/dishehara-tui-chords-4399394"
    driver.get(website)
    print("Loading : "+ website)
    listOfKeys = driver.find_elements(by=By.XPATH, value='//nav[@aria-label="All artists"]//a')
    if(listOfKeys.__len__()>0):
        print("Found list of Keys")
    return listOfKeys