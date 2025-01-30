from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from util.saveToDatabase import saveArtist

def getSingleArtistsLinks(link:str,id:int,letter:str,driver:WebDriver):
    currentLink=link
    lastPage=False
    print(f"loading from {letter}")
    while(not lastPage):
        print(f"Page Loading From {currentLink}")
        driver.get(currentLink)
        listOfArtistsInPage = driver.find_elements(by=By.XPATH, value='//article/div/div/div/span/a')
        for artist in listOfArtistsInPage:
            print(f"Saving Artist {artist.text.encode('utf-8')}")
            saveArtist(artist)
        lastLink=driver.find_elements(by=By.XPATH, value='//main/div/div/div//a[last()]')
        if( lastLink.__len__()>0 and (lastLink[lastLink.__len__()-1].text=="NEXT >")):
            print("Loading Next Page")
            currentLink=lastLink[lastLink.__len__()-1].get_attribute("href")
        else:
            lastPage=True

            
        
