import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.bewakoof.com/men-t-shirts')

soup = BeautifulSoup(response.content, 'html.parser')

posts = soup.find_all(class_="productCardBox")
prefix = "https://www.bewakoof.com"


for post in posts:
      title = post.find('h3').get_text().replace('\n', '')
      price = post.select('.discountedPriceText')[0].get_text()
      link = prefix + post.find_parent('a')['href']
      print(title,price,link)

with open('shirt.csv', 'w', encoding="utf-8") as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Title', 'Price', 'Link']
  csv_writer.writerow(headers)

  for post in posts:
      title = post.find('h3').get_text().replace('\n', '')
      price = post.select('.discountedPriceText')[0].get_text()
      link = prefix + post.find_parent('a')['href']
      csv_writer.writerow([title, price, link])