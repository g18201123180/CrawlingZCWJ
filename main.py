import json

from get_law import get_law
from get_one_page import get_one_page
import tqdm

links = []

# 更新链接
# get_one_page(links, "ef217aa7", "法律法规", 4)
# get_one_page(links, "14619177", "上级文件", 8)
# get_one_page(links, "3dea70b1", "本局规范性文件", 23)
# get_one_page(links, "5bbd66eb", "本局其他文件", 156)
# with open('links.json', 'w', encoding='UTF-8') as f:
#     json.dump(links, f)

with open('links.json') as f:
    links = json.load(f)

with open('error.log', 'w') as f:
    for link in tqdm.tqdm(links, desc='文件生成', unit="file"):
        try:
            get_law(link['title'], link['url'])
        except Exception as e:
            f.write(link['title'] + "\t" + link['url'] + "\t" + str(e) + "\n")
