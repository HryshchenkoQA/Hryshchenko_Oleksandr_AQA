import xml.etree.ElementTree as ET


class Moovie:
    def __init__(self, title, format, year, raiting, description, category):
        self.title = title
        self.format = format
        self.year = year
        self.raiting = raiting
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path):
        tree = ET.parse(path)
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

    @classmethod
    def xml_to_string(cls, path):
        tree = ET.parse('films.xml')
        root = tree.getroot()
        xml_to_string = ET.tostring(root)
        print(xml_to_string)


movies = Moovie.from_xml("films.xml")
for movie in movies:
    print(movie.title)

movie2 = Moovie.xml_to_string('films.xml')
print(movie2)