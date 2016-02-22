from bs4 import BeautifulSoup
import requests
import urllib


xunlei_url = 'http://521xunlei.com/'

if __name__ == '__main__':
    r = requests.get(xunlei_url + 'portal.php')
    print(type(r.text))
    if r.status_code != 200:
        print('打开url失败')
        exit()

    souped_text = BeautifulSoup(r.text)
    block = souped_text.find('div', id = 'portal_block_62_content')
    link_tags = block.find_all('a')
    for link_tag in link_tags:
        if link_tag.get('title') != None:
            link_url = urllib.parse.urljoin(xunlei_url, link_tag['href'])
            resp = requests.get(link_url)
            if resp.status_code != 200:
                print('open failed')
                continue
            soup = BeautifulSoup(resp.text)
            td_tag = soup.find('td', class_ = 't_f')
            fonts = td_tag.find_all('font', size = '4')
            for font in fonts:
                print(font.text)