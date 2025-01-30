from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from util.saveToDatabase import saveSongLink



def loadSingleLinks(rootUrl:str,driver:WebDriver,artistName:str):
    currentLink=rootUrl
    lastPage=False
    print(f"Loading Artist {artistName}")
    while(not lastPage):
        print(f"Page Loading From {currentLink}")
        driver.get(currentLink)
        rowsOfSongsInPage = driver.find_elements(by=By.XPATH, value='//section/article/div/div')
        print(f"number of rows {rowsOfSongsInPage.__len__()}")
        for row in rowsOfSongsInPage:
            type=row.find_element(by=By.XPATH,value=".//div[3]").text
            if(type == "Chords"):
                name=row.find_element(by=By.XPATH,value=".//header//a").text
                link=row.find_element(by=By.XPATH,value=".//header//a").get_attribute("href")
                saveSongLink(name=name,artistName=artistName,link=link)
        lastLink=driver.find_elements(by=By.XPATH, value='//section/div/div//a[last()]')
        if(lastLink.__len__()>0 and (lastLink[lastLink.__len__()-1].text=="NEXT >")):
            print("Loading Next Page")
            currentLink=lastLink[lastLink.__len__()-1].get_attribute("href")
        else:
            lastPage=True        
            
    return