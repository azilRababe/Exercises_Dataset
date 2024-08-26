import requests
from bs4 import BeautifulSoup

# abs should be replaced with the muscle you want to scrape (we need to make this dynamic)
url = 'https://fitnessprogramer.com/exercise-primary-muscle/abs/' 

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'lxml')
    
    articles = soup.find_all('div', class_='thumbnails')

    for article in articles:
       
        alt = article.find('img')['alt']
        link = article.find('img')['src']
        
       
        print(f"alt: {alt}") # this will print the alt attribute of the image
        print(f"link: {link}") # this will print the src attribute of the image
        print("-" * 40) # this will print a line of dashes for separation

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
