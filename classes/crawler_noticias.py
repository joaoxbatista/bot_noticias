#-*- coding: utf-8 -*-
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup

class CrawlerNoticia:
	def __init__(self, browser = webdriver.Chrome(), url = 'https://diarioarapiraca.com.br/editorias/arapiraca'):
		self.browser = browser
		self.url = url
		self.noticias = []
		self.site = 'diarioarapiraca.com.br'

	def proxima_pagina(self, page):
		self.url = 'https://diarioarapiraca.com.br/editorias/arapiraca/' + str(page)

	def get_noticia(self, url = ''):
		if(not url):
			self.browser.get(self.url)
		else:
			self.browser.get(url)

		noticias = self.browser.find_elements_by_css_selector('#noticias > ul > li')
		
		for noticia in noticias:
			noticia_html = noticia.get_attribute('innerHTML')
			noticia_soup = BeautifulSoup(noticia_html, 'html.parser')

			titulo = noticia_soup.select_one('.titulo').text
			url = noticia_soup.select_one('.titulo > a').get('href')
			data = noticia_soup.select_one('.data').text
			
			objeto_noticia = {
				"titulo": titulo,
				"data": data,
				"url": url
			}
			self.noticias.append(objeto_noticia)

	def get_noticias(self, page_quantity):
		for i in range(1, page_quantity+1):
			self.proxima_pagina(i)	
			time.sleep(4)
			self.get_noticia()
								

	def ler_json(self): 
		with open('data/noticias.json') as json_file:
			data = json.load(json_file)
			for site in data:
				if site['site'] == self.site: 
					self.noticias = site['noticias'] 
					

	def salvar_json(self):
		with open('data/noticias.json') as json_file:
			data = json.load(json_file)
			existe = False
			for site in data:
				if site['site'] == self.site: 
					site['noticias'] = self.noticias
					existe = True
			
			if not existe:
				data.append({'site': self.site, 'noticias': self.noticias})


			with open('data/noticias.json', 'w') as outfile:
				json.dump(data, outfile)
