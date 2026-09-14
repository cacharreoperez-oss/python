class File:
    def __init__(self, path: str):
        self.path = path
        self.content = []

    def add_content(self, content):
        self.content.append(content)

    @property
    def size(self):
        total = 0
        for item in self.content:
            total += len(item)
        return total

    @property
    def info(self):
        return f"{self.path} [size={self.size}B]"



class MediaFile(File):
    def __init__(self, path: str, codex: str, geoloc: tuple, duration: int):
        super().__init__(path)
        self.codex = codex
        self.geoloc = geoloc
        self.duration = duration

    @property
    def info(self):
        return (
            f"{super().info}\n"
            f"Codec: {self.codex}\n"
            f"Geolocalization: {self.geoloc}\n"
            f"Duration: {self.duration}s"
        )




class VideoFile(MediaFile):
    def __init__(self, path: str, codex: str, geoloc: tuple, duration: int, dimension: tuple):
        super().__init__(path, codex, geoloc, duration)
        self.dimension = dimension

    @property
    def info(self):
        return (
            f"{super().info}\n"
            f"Dimensions: {self.dimension}"
        )


    