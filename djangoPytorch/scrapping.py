import requests
from bs4 import BeautifulSoup
from csv import writer
import pandas as pd
from PIL import Image
import base64
from io import BytesIO
from base64 import b64decode
import os
from models.models import StoreImage

def scrap():
    print("here")
    urls = ['https://www.ndtv.com/topic/bangladesh-disaster', 'https://www.ndtv.com/topic/bangladesh-flood']

    href_url = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        p_tag = soup.find_all('p', {'class' : 'header fbld'})
        for a in p_tag:
            children = a.findChildren("a" , recursive=True)
            for h in children:
                href_url.append(h['href'])
            


    count = 0
    for ur in href_url:
        response = requests.get(ur)
        soup = BeautifulSoup(response.text,'html.parser')
        div = soup.find('div', {'class' : 'ins_instory_dv_cont lazyload'})
        image_url = div.img['data-src']
        img = Image.open(requests.get(image_url, stream = True).raw)
        img_name = 'image_'+str(count)+'.png'
        
        imgs = StoreImage(
            image_name=img_name,
            photo=image_url
        )
        imgs.save()
        count = count + 1

    print("Done Scrapping!!")        




