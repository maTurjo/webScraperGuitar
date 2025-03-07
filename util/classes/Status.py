class Status:
    def __init__(
        self,
        letterLinksRecovered: bool,
        initialized: bool,
        linkLoadingStarted: bool,
        nowLoadingLetter: str,
        nowLoadingId: int,
        artistsLoadingFinished:bool,
        currentArtistId:int,
        linkDbInitiated:bool,
    ):
        self.letterLinksRecovered = letterLinksRecovered
        self.initialized = initialized
        self.linkLoadingStarted = linkLoadingStarted
        self.nowLoadingLetter = nowLoadingLetter
        self.nowLoadingId = nowLoadingId
        self.artistsLoadingFinished = artistsLoadingFinished
        self.currentArtistId = currentArtistId
        self.linkDbInitiated = linkDbInitiated
