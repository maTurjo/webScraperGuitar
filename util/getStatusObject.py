import json
from pathlib import Path
from .classes.Status import Status

# from classes import Status
def getStatusObject()->Status:
    root=Path(__file__).parent.parent.__str__()
    filePath=Path("/meta/status.json").__str__()
    file = open(root+filePath)
    statusJson = json.load(file)
    statusObject = Status(letterLinksRecovered=statusJson["letterLinksRecovered"],
                          initialized=statusJson["initialized"],
                          linkLoadingStarted=statusJson["linkLoadingStarted"],
                          nowLoadingLetter=statusJson["nowLoadingLetter"],
                          nowLoadingId=statusJson["nowLoadingId"]
                          )
    return statusObject

def setStatusObject(status:Status):
    root=Path(__file__).parent.parent.__str__()
    filePath=Path("/meta/status.json").__str__()
    file = open(root+filePath,'w')
    json.dump(status.__dict__,file)
    print("Status Updated Successfully")
    
    
