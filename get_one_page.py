import re

from bs4 import BeautifulSoup
import tqdm
from get_response import get_response


def get_one_page(links, code, keyword, page_num):
    for i in tqdm.tqdm(list(range(1, page_num + 1)), desc=code, unit="page"):
        url = "http://sthjj.beijing.gov.cn/bjhrb/index/xxgk69/zfxxgk43/fdzdgknr2/zcfb/325821937/" + code + "-" + str(
            i) + ".html"
        response = get_response(url)

        # 用BeautifulSoup解析html
        soup = BeautifulSoup(response.read(), 'html.parser')

        divs = soup.find_all('div', class_='h_mod qs_clear')

        for div in divs:
            if re.search(keyword, div.text):
                aTag = div.next_sibling.next_sibling.find('ul').find_all('a')
                for tmp in aTag:
                    links.append({'title': tmp['title'], "url": 'http://sthjj.beijing.gov.cn/' + tmp['href']})
