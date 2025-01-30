from selenium import webdriver
from listOfSongs import listOfSongs
from util.getStatusObject import getStatusObject, setStatusObject
from functionals.loadLetterLinks import loadLetterLinks
from functionals.initialize import initialize,initiateLinkTable
from functionals.getLetterLinkDB import getLetterLinkDB
from functionals.getSingleLinks import getSingleArtistsLinks
from functionals.loadSingleLinks import loadSingleLinks
from functionals.getArtistLinkDB import getArtistLinkDB
from options import options
from util.saveToDatabase import saveLetter
from util.getRowCount import getRowCount
import time


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

if status_object.initialized and status_object.letterLinksRecovered:
    status_object.linkLoadingStarted = True
    setStatusObject(status_object)
if not status_object.artistsLoadingFinished:
    if status_object.linkLoadingStarted:
        if status_object.nowLoadingId == 0:
            status_object.nowLoadingId = 1
            setStatusObject(status_object)
        rowCount = getRowCount("letterLinks")
        driver = webdriver.Chrome(options=options)
        for id in range(1, rowCount + 1):
            if not id < status_object.nowLoadingId:
                row = getLetterLinkDB(id)
                id = row[0]
                letter = row[1]
                link = row[2]
                getSingleArtistsLinks(link, id, letter, driver)
                print(link)
                status_object.nowLoadingId = status_object.nowLoadingId + 1
                status_object.nowLoadingLetter = link[1]
                setStatusObject(status_object)

if status_object.artistsLoadingFinished:
    driver = webdriver.Chrome(options=options)
    artistCount = getRowCount("artistsLinks")
    currentArtistId = status_object.currentArtistId
    if(not status_object.linkDbInitiated):
        initiateLinkTable()
        status_object.linkDbInitiated=True
        setStatusObject(status_object)
    if currentArtistId == 0:
        currentArtistId = currentArtistId + 1
    while currentArtistId <= artistCount:
        try:
            row = getArtistLinkDB(currentArtistId) 
            id=row[0]
            artistName=row[1]
            artistLink=row[2]
            loadSingleLinks(rootUrl=artistLink,driver=driver,artistName=artistName)
            currentArtistId = currentArtistId + 1
        except:
            status_object.currentArtistId = currentArtistId
            setStatusObject(status_object)
            print("exception Occured")
            print(f"status saved {status_object.__dict__}")
