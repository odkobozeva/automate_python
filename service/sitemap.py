import pytest
import requests
from bs4 import BeautifulSoup


@pytest.mark.parametrize('url', [
'http://dev.2bitcoins.ru/sitemap_index.xml',
# 'http://dev.2bitcoins.ru/post-sitemap1.xml',
# 'http://dev.2bitcoins.ru/post-sitemap2.xml',
# 'http://dev.2bitcoins.ru/post-sitemap3.xml',
# 'http://dev.2bitcoins.ru/post-sitemap4.xml',
# 'http://dev.2bitcoins.ru/post-sitemap5.xml',
# 'http://dev.2bitcoins.ru/post-sitemap6.xml',
# 'http://dev.2bitcoins.ru/post-sitemap7.xml',
# 'http://dev.2bitcoins.ru/page-sitemap.xml',
# 'http://dev.2bitcoins.ru/post_tag-sitemap.xml',
# 'http://dev.2bitcoins.ru/author-sitemap.xml'
])
def test_sitemap(url):
    response = requests.get(url, auth=('****', '****')).text
    items = BeautifulSoup(response, 'html.parser').find_all('loc')
    handle = open("dev.txt", "a")
    for item in items:
        handle.write(f'\'{item.text}\',\n')
    handle.close()
