import requests
from bs4 import BeautifulSoup
import variables.url

apple_with_robots = variables.url.url_apple_with_robots
apple_without_robots = variables.url.url_apple_without_robots
hinews_with_robots = variables.url.url_hinews_with_robots
hinews_without_robots = variables.url.url_hinews_without_robots
android_with_robots = variables.url.url_android_with_robots
android_without_robots = variables.url.url_android_without_robots

url = ['appleinsider.ru/',
'appleinsider.ru/page/8',
'appleinsider.ru/page/38',
'appleinsider.ru/page/180',
'appleinsider.ru/iphone',
'appleinsider.ru/iphone/page/5',
'appleinsider.ru/accessories',
'appleinsider.ru/accessories/page/10',
'appleinsider.ru/ios',
'appleinsider.ru/ios/page/30',
'appleinsider.ru/ipad',
'appleinsider.ru/ipad/page/80',
'appleinsider.ru/safari',
'appleinsider.ru/safari/page/2',
'appleinsider.ru/obzory-zheleza',
'appleinsider.ru/obzory-zheleza/page/9',
'appleinsider.ru/tag/prilozhenie',
'appleinsider.ru/tag/prilozhenie/page/18',
'appleinsider.ru/tag/apple',
'appleinsider.ru/tag/apple/page/32',
'appleinsider.ru/tag/texnologii',
'appleinsider.ru/tag/texnologii/page/48',
'appleinsider.ru/tag/perevod-biografii-stiva-dzhobsa',
'appleinsider.ru/tag/tvitter',
'appleinsider.ru/author/ivfilon',
'appleinsider.ru/author/gellert',
'appleinsider.ru/author/bogdanov'
'appleinsider.ru/author/gellert/page/8',
'appleinsider.ru/author/svarogstin',
'appleinsider.ru/author/appleinsider-ru',
'appleinsider.ru/mac-pro/apple-nachala-oficialnye-prodazhi-novogo-mac-pro-v-rossii.html',
'appleinsider.ru/iphone/apple-poluchaet-66-vsex-deneg-rynka-smartfonov.html',
'appleinsider.ru/eto-interesno/pochemu-ekrannyj-touch-id-eto-put-apple-k-innovaciyam.html',
'appleinsider.ru/hardware/thunderbolt-4-protiv-usb-4-ostanetsya-tolko-odin.html',
'appleinsider.ru/apple-tv/o-kakix-osobennostyax-apple-tv-vy-prosto-obyazany-znat.html',
'appleinsider.ru/apple-v-licax/stiv-voznyak-rasskazal-pro-svoyo-lyubimoe-ustrojstvo-ot-apple.html',
'appleinsider.ru/apple-v-licax/eks-marketolog-macintosh-rasskazal-kak-uderzhatsya-na-rabote-v-apple.html',
'appleinsider.ru/analysis/vazhnaya-funkciya-apple-watch-okazalas-bespoleznoj-dlya-mnogix-polzovatelej.html'
]



def test_get_description():
    # url = apple_with_robots + apple_without_robots
    i = 0
    while i < len(url):
        response = requests.get('https://' + url[i]).text
        meta_description = BeautifulSoup(response, features="lxml").find('meta', attrs={'name': 'description'})
        if meta_description is None:
            meta_content = 'None'
        else:
            meta_content = meta_description["content"]
        print(f'"{url[i]}" : "{meta_content}",')
        i += 1


def test_get_title():
    url = apple_with_robots + apple_without_robots
    i = 0
    while i < len(url):
        response = requests.get('https://' + url[i]).text
        meta_title = BeautifulSoup(response, features="lxml").find('meta', attrs={'name': 'title'})
        if meta_title is None:
            meta_content = 'None'
        else:
            meta_content = meta_title["content"]
        print(f'"{url[i]}" : "{meta_content}",')
        i += 1

def test_get_robots():
    url = apple_with_robots + apple_without_robots
    i = 0
    while i < len(url):
        response = requests.get('https://' + url[i]).text
        meta_robots = BeautifulSoup(response, features="lxml").find('meta', attrs={'name': 'robots'})
        if meta_robots is None:
            meta_content = 'None'
        else:
            meta_content = meta_robots["content"]
        print(f'"{url[i]}" : "{meta_content}",')
        i += 1


def test_get_canonical():
    url = apple_with_robots + apple_without_robots
    i = 0
    while i < len(url):
        response = requests.get('https://' + url[i]).text
        meta = BeautifulSoup(response, features="lxml").find('link', attrs={'rel': 'canonical'})
        if meta is None:
            meta_content = 'None'
        else:
            meta_content = meta['href']
        print(f'"{url[i]}" : "{meta_content}",')
        i += 1
