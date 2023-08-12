from lesson16.mona_lisa_singleton import singleton
@singleton
class MonaLisa:
    def __init__(self, age, author, size):
        self.age = age
        self.author = author
        self.size = size
        self.smile = True

mona_lisa_1 = MonaLisa()


