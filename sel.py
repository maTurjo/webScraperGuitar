from selenium import webdriver
from listOfSongs import listOfSongs
from util.getStatusObject import getStatusObject, setStatusObject
from functionals.loadLetterLinks import loadLetterLinks
from functionals.initialize import initialize
from functionals.getLetterLinkDB import getLetterLinkDB
from functionals.getSingleLinks import getSingleArtistsLinks
from options import options
from util.saveToDatabase import saveLetter
from util.getRowCount import getRowCount


driverPath = "C:/Users/matur/Downloads/chrome-win64/chrome.exe"

status_object = getStatusObject()

##Initializing project and creating tables
if not status_object.initialized:
    initialize()
    status_object.initialized = True
    setStatusObject(status_object)


if not status_object.letterLinksRecovered:
    driver = webdriver.Chrome(options=options)
    listOfLetterLinks = loadLetterLinks(driver)
    for letter in listOfLetterLinks:
        saveLetter(letter)
    status_object.letterLinksRecovered = True
    setStatusObject(status_object)
    
if status_object.initialized & status_object.letterLinksRecovered:
    status_object.linkLoadingStarted = True
    setStatusObject(status_object)

if status_object.linkLoadingStarted:
    if status_object.nowLoadingId == 0:
        status_object.nowLoadingId = 1
        setStatusObject(status_object)
    rowCount = getRowCount("letterLinks")
    driver = webdriver.Chrome(options=options)
    for id in range(1,rowCount+1):
        if(not id<status_object.nowLoadingId):
            row=getLetterLinkDB(id)
            id=row[0]
            letter=row[1]
            link=row[2]
            getSingleArtistsLinks(link,id,letter,driver)
            print(link)
            status_object.nowLoadingId=status_object.nowLoadingId+1
            status_object.nowLoadingLetter=link[1]
            setStatusObject(status_object)
