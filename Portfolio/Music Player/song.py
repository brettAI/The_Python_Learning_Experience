class Song:
    def __init__(self,
                 songId,
                 duration,
                 uri,
                 title,
                 artist,
                 albumName,
                 year,
                 comment,
                 trackNumber,
                 genre):
        self.duration = duration
        self.uri = uri

        # ID3 Variables
        self.title
        self.artist
        self.albumName
        self.year
        self.comment
        self.trackNumber
        self.genre

    def getSongData(self):
        return duration, uri, title
