import json

from classes.crawler_noticias import CrawlerNoticia
from classes.gerador_imagens import GeradorImagem

crawler = CrawlerNoticia()
crawler.url = 'https://diarioarapiraca.com.br/editorias/arapiraca/'
crawler.get_noticias(4)

crawler.salvar_json()

gerador = GeradorImagem()
for noticia in crawler.noticias:
	gerador.gerar(noticia)
