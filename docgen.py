#!/usr/bin/python3
# Программа для генерации html-страниц из Markdown-документов
# (C) 2022 Michail Krasnov <linuxoid85@gmail.com>

import json
import markdown
import json

start_page = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Тестовая страница</title>
    </head>
    <body>
"""

end_page = "</body></html>"

class configuration():

    def __init__(self, config):
        self.config = config
    
    def __doc__(self):
        """
        Класс с функциями для получения данных из JSON-файлов
        """
    
    def get_all(self) -> dict:
        """
        Получение всех данных из JSON-файла
        """
        
        with open(self.config) as f:
            data = json.load(f)
        return data
    
    def get_param(self, param):
        """
        Получение указанного параметра из JSON-файла
        """
        
        data = self.get_all()
        return data[param]
    
    def set(self, data):
        """
        Установка новых значений всех параметров в JSON-конфиге
        """
        
        with open(self.config, "w") as f:
            data = json.dump(data, f, indent=4, ensure_ascii=True)
        
        with open(self.config) as f:
            data = json.load()
        return data

class generator():

    def __init__(self, page):
        self.page = page
    
    def gen(self):
        md = self.page + ".md"
        html = self.page + ".html"
        
        with open(md) as f:
            txt_md = f.read()
            txt_html = markdown.markdown(txt_md)
        
        with open(html, "w") as f:
            html = f"{start_page}{txt_html}\n{end_page}"
            f.write(html)

pages = configuration('conf.json').get_param('pages')

for page in pages:
    generator(page).gen()
