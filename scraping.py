import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.codementor.io/blog')

soup = BeautifulSoup(response.content, 'html.parser')

posts = soup.find_all(class_='post')

with open('posts.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Title', 'Date']
  csv_writer.writerow(headers)

  for post in posts:
    title = post.find(class_='post-title').get_text().replace('\n', '')
    date = post.select('.article-time')[0].get_text()
    csv_writer.writerow([title, date])
  
  
