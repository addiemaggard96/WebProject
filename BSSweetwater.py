import requests
from bs4 import BeautifulSoup
import datetime
import json


urlSW = 'https://www.sweetwater.com/store/search.php?s=electric+violin&Go=Search'
pageSW = requests.get(urlSW)
soupSW = BeautifulSoup(pageSW.content, 'lxml')

position = soupSW.find('div', class_='products')
itemURL = 'http://sweetwater.com/' + position.find('a').get('href')
title = itemURL.find('h1')
description = itemURL.find('a')
# price
# specs

print(title)
print(description)
#print(price)
#print(specs)
print(itemURL)















# item = item.next_sibling
# #nextSib gets next position at same level in tree
# #create a loop to go through everything
# for position in soupSW.find_all('a', class_='products')
#     if position.find('a').next_sibling and position.find('strong')
#         description = position.find('a').next_sibling.find('strong').string
#         print(description)


# pagination bottomPagination
#     paging oneDir
#         next
#urlSW=next