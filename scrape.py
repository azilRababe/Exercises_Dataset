import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0'
}

def get_content(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'lxml')
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None
    
data_list=[]

def get_url(query,page=1):
    while True:
        url=f'https://fitnessprogramer.com/exercise-primary-muscle/{query}/page/{page}/'
        # print(f"Scraping page {page} at URL: {url}")

        gifs = get_content(url).find_all('div', class_='thumbnails')

        for gif in gifs:
            title = gif.find('img')['alt']
            src = gif.find('img')['src']

            data_list.append({'title': title, 'src': src})
            

        next_page = get_content(url).find('a', class_='next') 
        if next_page and 'href' in next_page.attrs:
            page += 1
        else:
            # print("No more pages to scrape.")
            break       
    
data_list.clear() # clear the list before appending new data

def scrape(query):
    
    data=get_url(query)
    data=pd.DataFrame(data_list)

    print(data.head(10).to_string(index=False)) # for testing purposes
    # data.to_csv(f'{query}_exercises.csv', index=False) # uncomment this line to save the data to a csv file


# scrape('chest') # pass the muscle group you want to scrape