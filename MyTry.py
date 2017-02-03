# import requests
# from bs4 import BeautifulSoup
#
# # Scrape Amazon with requests
# urlAmazon = 'https://www.amazon.com/ref=nav_logo'
# pageAmazon = requests.get(urlAmazon)
#
# # Prepare for parsing Amazon with BeautifulSoup
# soupAmazon = BeautifulSoup(pageAmazon.content, 'lxml')
#
# position = soupAmazon.find('div', class_='s-results-list-atf') #'location of news brief in html')
# item = position.find('a').string
# #priceDollar = position.
# #priceCents =
# description = position.find('span', class_= 'topheadlinebody').string #'location of brief in html'
# # seller = description.split(' (AP) ') [0] #'location of apOffice in html'
# fullExplanation = 'hosted.ap.org' + position.find('a').get('href') #'location of fullStory in html'
#
# print(item)
# #print(priceDollar + '.' + priceCents)
# print(description)
# print(seller)
# print(fullExplanation)

