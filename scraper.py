import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0'
}

# Function to get the content of the webpage
def get_content(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'lxml')
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None
    
# Function to get the URL of the page
def get_url(query,page=1,datalist=[]):
    while True:
        url=f'https://fitnessprogramer.com/exercise-primary-muscle/{query}/page/{page}/'
        # print(f"Scraping page {page} at URL: {url}")

        gifs = get_content(url).find_all('div', class_='thumbnails')

        for gif in gifs:
            title = gif.find('img')['alt']
            src = gif.find('img')['src']
            datalist.append({
                'targetMuscle': query,
                'title': title,
                'src': src
            })
            
        next_page = get_content(url).find('a', class_='next') 
        if next_page and 'href' in next_page.attrs:
            page += 1
        else:
            # print("No more pages to scrape.")
            break       
    
targetMuscles=['full-body','neck','trapezius','shoulders','chest','back','biceps','triceps','forearm','abs','calf','erector-spinae','leg','hips','cardio']

allData=[]
for muscle in targetMuscles:
    datalist=[]
    get_url(muscle,1,datalist=datalist)
    allData.extend(datalist)

df=pd.DataFrame(allData, columns=['targetMuscle','title','src'],index=None)

# Save the data to a JSON file
df.to_json('data/gifs.json', orient='records') 