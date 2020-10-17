import bs4 as bs
import requests
import openpyxl

class zoeker:
    def __init__(self, provincie, stad):
        self.stad = stad
        self.provincie = provincie
        self.url = 'https://www.huizenzoeker.nl/koop/{}/{}/'.format(self.provincie, self.stad)

    def soup(self):
        
        access = requests.get(self.url).text
        html = bs.BeautifulSoup(access, 'html.parser')
        self.soup = html
        

    def adres(self):
        soup = self.soup
        adressen = soup.find_all('a', 'titel')
        adressen = adressen[1:]

        adressen = [adr.strong.text for adr in adressen]
        return adressen



    

    
        




            