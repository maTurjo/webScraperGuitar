import sqlite3
from pathlib import Path
from selenium.webdriver.remote.webelement import WebElement

def saveLetter(linkItem:WebElement):
    tableName="letterLinks"
    root=Path(__file__).parent.parent.__str__()
    databasePath=Path("/data/GuitarTabs.db").__str__()
    connect = sqlite3.connect(root+databasePath)
    sql = ''' INSERT INTO letterLinks(name,link) VALUES(?,?) '''
    cursor=connect.cursor()
    cursor.execute(sql,(linkItem.text,linkItem.get_attribute('href')))
    connect.commit()
    connect.close()
    return

def saveArtist(linkItem:WebElement):
    tableName="artistsLinks"
    root=Path(__file__).parent.parent.__str__()
    databasePath=Path("/data/GuitarTabs.db").__str__()
    connect = sqlite3.connect(root+databasePath)
    sql = ''' INSERT INTO artistsLinks(name,link) VALUES(?,?) '''
    cursor=connect.cursor()
    cursor.execute(sql,(linkItem.text.encode("utf-8"),linkItem.get_attribute('href').encode("utf-8")))
    connect.commit()
    connect.close()

def saveSongLink(name:str,artistName:str,link:str):
    tableName="songLinks"
    root=Path(__file__).parent.parent.__str__()
    databasePath=Path("/data/GuitarTabs.db").__str__()
    connect = sqlite3.connect(root+databasePath)
    sql = ''' INSERT INTO songLinks(name,artistName,link) VALUES(?,?,?) '''
    cursor=connect.cursor()
    cursor.execute(sql,(name.encode("utf-8"),artistName.encode("utf-8"),link.encode("utf-8")))
    connect.commit()
    connect.close()