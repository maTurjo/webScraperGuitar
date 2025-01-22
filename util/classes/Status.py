class Status:
    def __init__(self, letterLinksRecovered: bool,initialized:bool,linkLoadingStarted:bool,nowLoadingLetter:str,nowLoadingId:int):
        self.letterLinksRecovered = letterLinksRecovered
        self.initialized = initialized
        self.linkLoadingStarted = linkLoadingStarted
        self.nowLoadingLetter = nowLoadingLetter
        self.nowLoadingId = nowLoadingId