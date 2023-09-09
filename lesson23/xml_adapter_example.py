from xml.etree import ElementTree

class Moovie:
    def __init__(self, title, format, year, raiting, description, category):
        self.title = title
        self.format =format
        self.year = year
        self.raiting = raiting
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        for genre in collection:
            for decade in genre:
                for movie in decade:
                    movies.append(cls(
                        movie.attrib['title'],
                        movie.find('format').text,
                        movie.find('year').text,
                        movie.find('rating').text,
                        movie.find('description').text,
                        genre.attrib['category']
                    ))
        return movies

movies = Moovie.from_xml("films.xml")
for movie in movies:
    print(movie.title)
