import requests


from bs4 import BeautifulSoup



class EgyBest:
    def getElementText(self,name, dict, soup):
        elements = soup.find(name, dict)
        print(elements.text)
        return elements.text

    def getElement(self,name, dict, soup):
        elements = soup.find(name, dict)
        return elements

    def getElementContent(self,name, dict, key, soup):
        elements = soup.find(name, dict)
        print(elements[key])
        return elements[key]

    def __init__(self,name_movie):
        self.name_movie = name_movie
        self.name_movie = self.name_movie.replace( ' ' , '+' )

        self.url = 'https://grey.egybest.network/explore/?q=NameMovie'
        self.url = self.url.replace('NameMovie', self.name_movie)

        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, "html.parser")

        self.url = self.getElementContent('a', {'class': 'movie'}, 'href', soup)

        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, "html.parser")

        # name
        self.nameMovie = self.getElementText('span', {'itemprop': 'name'}, soup)
        # date
        self.dateMovie = self.getElement('div', {'class': 'movie_title tam'}, soup)
        self.dateMovie = self.getElementText('a', {}, self.dateMovie)
        # poster
        self.posterurl = self.getElementContent('img', {'itemprop': 'image'}, 'src', soup)
        # table
        table = soup.find('table', {'class': 'movieTable full'}).find_all('tr')
        # language
        self.language = table[1].find_all('a')[0].text
        print(self.language)
        # country
        self.country = table[1].find_all('a')[1].text
        print(self.country)
        # rating
        self.rating = self.getElementText('span', {'itemprop': 'ratingValue'}, soup)
        # type
        typesTable = table[3].find_all('a')
        self.types = {3, 5, 5}
        self.types.clear()
        for type in typesTable:
            self.types.add(type.text)
        print(self.types)
        # story
        self.story = soup.find_all('div', {'class': 'mbox'})[3].text
        print(self.story)













