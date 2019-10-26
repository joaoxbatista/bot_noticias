#-*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os
import textwrap
import time
from datetime import datetime

class GeradorImagem: 

	def __init__(self, width = 1080, height = 720, filename = 'imagem.png'):
		self.width = width
		self.height = height
		self.filename = filename

	def escrever_texto(self,draw, texto, largura_maxima = 60, margin_top = 100, font_size = 30):
		wrap_text = textwrap.wrap(texto, width=largura_maxima)
		font = ImageFont.truetype(r"C:\Users\jhonxbatista\Desktop\bot_noticias\fonts\Jomolhari-Regular.ttf", font_size)
		for i in range(len(wrap_text)):
			draw.text((120, margin_top),wrap_text[i],font=font, fill=(255, 255, 255))
			margin_top += font_size
							
	def gerar(self, noticia = {"titulo": "lorem ipsum dolar text of example the case of test is true is correct work lorem ipsum dolar text of example the case of test is true is correct work lorem ipsum dolar text of example the case of test is true is correct worklorem ipsum dolar text of example the case of test is true is correct worklorem ipsum dolar text of example the case of test is true is correct worklorem ipsum dolar text of example the case of test is true is correct worklorem ipsum dolar text of example the case of test is true is correct work", "data": "20/01/2019 20:40", "url": "google.com.br"}, filename=""):
		img = Image.open(r'C:\Users\jhonxbatista\Desktop\bot_noticias\imagens\backgroundd.jpg').convert('RGB')
		draw = ImageDraw.Draw(img)
		self.escrever_texto(draw, noticia['data'], 45, 100, 40)
		self.escrever_texto(draw, noticia['titulo'], 26, 160, 68)
		self.escrever_texto(draw, noticia['url'], 45, 620, 40)

		if (len(noticia['titulo']) > 20):
			filename = noticia['data'].replace("/", "_").replace(':', '_') + noticia['titulo'].replace(" ", "_")[:20] + str('.png')
		else: 
			filename = noticia['titulo'].replace(" ", "_")[:20] + str('.png')
			
		img.save('./imagens/' + filename)
		




