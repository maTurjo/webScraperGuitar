import selenium
from selenium import webdriver
from options import options
from selenium.webdriver.common.by import By


def songScrapper():
    driver = webdriver.Chrome(options=options)
    link="https://tabs.ultimate-guitar.com/tab/louis-armstrong/what-a-wonderful-world-chords-1412250"
    driver.get(link)
    songNameXpath="//header//h1"
    artistNameXpath="//section/header//span/a"
    statsStringXpath="//main/div[3]/article[1]/section[1]/div[2]" #13,941 views, added to favorites 745 times
    detailsTableXpath="//table" #difficulty ,tuning,key,capo
    authorXpath="//span[@data-type='info']/a" #author link
    infoStringXpath="//article[1]/section[1]/div[4]/span[2]" #2 contributors total, last edit on Sep 16, 2024
    songHTMLXpath="//code"
    
    songName=driver.find_element(by=By.XPATH,value=songNameXpath).text
    artistName=driver.find_element(by=By.XPATH,value=artistNameXpath).text
    statsString=driver.find_element(by=By.XPATH,value=statsStringXpath).text
    detailsTable=driver.find_element(by=By.XPATH,value=detailsTableXpath)
    author=driver.find_element(by=By.XPATH,value=authorXpath).text
    infoString=driver.find_element(by=By.XPATH,value=infoStringXpath).text
    songHtml=driver.find_element(by=By.XPATH,value=songHTMLXpath).get_attribute("innerHTML")
    
    detailRows=detailsTable.find_elements(by=By.XPATH,value=".//tr")
    detailsDictionary=dict()
    for row in detailRows:
        key=row.find_element(by=By.XPATH,value=".//th").text[:-1]
        value=row.find_element(by=By.XPATH,value=".//td").text
        detailsDictionary[key]=value
    
    print(detailsDictionary)
    print(f"song Name is {songName}")
    print(f"aritst Name is {artistName}")
    print(f"author Name is {author}")
    print(f"stat: {statsString}")
    # print(f"details: {detailsTable}")
    print(f"infoString: {infoString}")
    # print(f"song: {songHtml}")
    
    driver.get(link)
    
songScrapper()
    