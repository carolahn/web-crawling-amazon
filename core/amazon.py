from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from bs4 import BeautifulSoup

class Bot:
    
    def __init__(self):
        
        binary = FirefoxBinary('/usr/bin/firefox') # path do executável do firefox
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.url_base = 'https://www.amazon.com.br/'


    def search(self, query):
        
        self.driver.get(self.url_base)

        sleep(2)
        
        search_input = self.driver.find_element_by_id('twotabsearchtextbox')
        search_input.send_keys(query)
        
        button_search = self.driver.find_element_by_css_selector('.nav-input[value=Ir]')
        button_search.click()

        sleep(2)

    
    def get_items_search(self):
        
        page_source = self.driver.page_source # o htmml da pág
        
        parser = BeautifulSoup(page_source, 'html.parser') # (html, tipo de parser)
        
        items = parser.select('div[data-component-type=s-search-result]')
    
        results = []

        for item in items:
            title = item.select_one('.a-link-normal.a-text-normal') # pega a tag a

            url = title.get('href') # pega o atribulo href

            title = title.text # pega só o texto
            title = title.replace('\n', '')

            price = item.select_one('.a-offscreen')
            
            if not price:
                continue
            
            price = price.text
            price = price.replace('.','').replace('R$', '').replace(',', '.') # trocar a virgula por ponto, para poder transf para float
            price = float(price)
            
            result = {'title': title, 'price': price, 'url': self.url_base + url}
            results.append(result)
            
        return results
            
            
            
            