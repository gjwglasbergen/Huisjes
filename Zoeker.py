import bs4 as bs
import requests
import pandas as pd

class zoeker:
    def __init__(self, provincie, stad):
        self.stad = stad
        self.provincie = provincie
        self.url = 'https://www.huizenzoeker.nl/koop/{}/{}/'.format(self.provincie, self.stad)

    def soup(self):
        
        access = requests.get(self.url).text
        html = bs.BeautifulSoup(access, 'html.parser')

        return html

    
        




            